__author__ = 'Tom'

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^roster/(?P<team_id>\d+)$', 'nhl.views.roster', name='roster'),
)