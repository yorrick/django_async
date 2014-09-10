from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django_async.ems_messages.rest import router


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_async.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^', include('django_async.ems_messages.urls', namespace="message")),
)
