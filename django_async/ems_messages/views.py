# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django_async.ems_messages.models import Message
from django.views import generic
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.cache import get_cache_key

import random
import logging

from django_async.ems_messages.api import save_message, message_list


logger = logging.getLogger(__name__)


class DetailView(generic.DetailView):
    model = Message
    template_name = 'messages/detail.html'
    context_object_name = 'message'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['user', 'source', 'destination', 'content', ]

    def clean_content(self):
        content = self.cleaned_data['content']
        logger.debug('Cleaning content field: {}'.format(content))

        if 'toto' in content:
            raise ValidationError(_("This content is not allowed"))
        else:
            return content


@cache_page(60 * 15)
def index(request):

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            logger.debug('Form is valid, message is {}'.format(form.instance))
            save_message(form.instance)

            # basic behavior: invalidate page cache
            key = get_cache_key(request)
            cache.delete(key)

            return HttpResponseRedirect(reverse('message:index', args=tuple()))
        else:
            logger.debug('Form is not valid: {}'.format(form.errors))

            context = create_default_context()
            context.update({'form': form, 'form_error': True})

            return render(request, 'messages/index.html', context)

    else:
        # creation test is faster by already binding form with default values
        default_message = Message(
            user=User.objects.all()[0],
            source="the source",
            destination="the dest",
            content="the content {}".format(random.randint(1, 10)))

        context = create_default_context()
        context.update({'form': MessageForm(instance=default_message), 'form_error': False})

        return render(request, 'messages/index.html', context)


def create_default_context():
    return {
        'message_list': message_list(),
    }
