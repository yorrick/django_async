# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.test import TestCase
from django_async.ems_messages.api import save_message
from django_async.ems_messages.models import Message
from django.core.urlresolvers import reverse

from django_async.utils import language


class ApiTest(TestCase):

    fixtures = ['users.json', 'messages.json']

    def test_save(self):
        """
        Test that save is working
        """
        message = Message(user_id=1, source="the source", destination="the dest", content="the content")

        self.assertTrue(message.id is None)
        returned_message = save_message(message)
        self.assertTrue(returned_message.id is not None)


class ViewTest(TestCase):

    fixtures = ['users.json', 'messages.json']

    def test_index_display(self):
        response = self.client.get(reverse('message:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")
        self.assertEqual(len(response.context['message_list']), 2)

    def test_french_index_display(self):
        with language('fr'):
            response = self.client.get(reverse('message:index'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Bienvenue")
            self.assertEqual(len(response.context['message_list']), 2)

    def test_create_new_message(self):
        data = {
            'user': 1,
            'source': 'the source',
            'destination': 'the destination',
            'content': 'the content',
        }

        response = self.client.post(reverse('message:index'), data)
        # redirect means success
        self.assertEqual(response.status_code, 302)

    def test_form_validation(self):
        data = {
            'user': 1,
            'source': 'the source',
            'destination': 'the destination',
            'content': 'toto content',
            }

        response = self.client.post(reverse('message:index'), data)
        # 200 means error
        self.assertEqual(response.status_code, 200)

