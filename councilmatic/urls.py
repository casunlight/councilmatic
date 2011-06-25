from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import ListView
import phillyleg.models

import subscriptions.views
import haystack.views

urlpatterns = patterns('',
    # Example:
    #(r'^philly_legislative/', include('philly_legislative.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', admin.site.urls),

    (r'^/$', 'phillyleg.views.index'),
    (r'^subs/$', 'phillyleg.views.subscribe'),
    (r'^subs/create/$', 'phillyleg.views.create'),
    (r'^subs/unsubscribe/$', 'phillyleg.views.unsubscribe'),
    #(r'^subs/(?P<subscription_id>\d+)/$', 'phillyleg.views.edit'),
    (r'^subs/delete/$', 'phillyleg.views.delete'),
    
    (r'^legislation/files', ListView.as_view(
        model=phillyleg.models.LegFile,
        template_name='legfile_list.html',
        context_object_name='legfile_list')),
    
    (r'^search$', subscriptions.views.SearchView()),
    (r'^subscribe$', subscriptions.views.SubscribeToSearchView.as_view()),
    (r'^(?P<subscription_id>\d+)/$', 'phillyleg.views.dashboard'),
#    (r'^search/', include('haystack.urls')),
)