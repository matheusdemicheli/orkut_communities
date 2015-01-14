from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', 'find.views.home', name='home'),
    url(r'^results/(?P<term>[\w\W ]+)/$', 'find.views.results', name='results'),
    url(r'^help/$', 'find.views.help', name='help')
)
