#====================================
#Project: Rosters
#App: Clipboard
#Doc: urls.py
#====================================

from django.conf.urls import patterns, include, url
from clipboard import views

urlpatterns = patterns('',
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^coaches/$', views.coaches, name='coaches'),
    url(r'^athletes/$', views.athletes, name='athletes'),
    url(r'^teamView/(?P<team_id_id>\d+)/$', views.teamView, name='teamView'),
)