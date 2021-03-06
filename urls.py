from __future__ import unicode_literals
from django.conf.urls import url, include
from . import views

local_urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^request_pilot_standings/(?P<character_id>\d+)/', views.request_pilot_standings,
        name='request_pilot_standing'),
    url(r'^remove_pilot_standings/(?P<character_id>\d+)/', views.remove_pilot_standings,
        name='remove_pilot_standing'),
    url(r'^request_corp_standings/(?P<corp_id>\d+)/', views.request_corp_standings,
        name='request_corp_standing'),
    url(r'^remove_corp_standings/(?P<corp_id>\d+)/', views.remove_corp_standings,
        name='remove_corp_standing'),

    url(r'^view/pilots/$', views.view_pilots_standings, name='view_pilots'),
    url(r'^view/pilots/json/$', views.view_pilots_standings_json, name='view_pilots_json'),
    url(r'^view/pilots/download/$', views.download_pilot_standings, name='download_pilots'),
    url(r'^view/corps/$', views.view_groups_standings, name='view_groups'),
    url(r'^view/corps/json$', views.view_groups_standings_json, name='view_groups_json'),
    url(r'^manage/$', views.manage_standings, name='manage'),
    url(r'^manage/requests/$', views.manage_get_requests_json, name='manage_get_requests_json'),
    # Should always follow the path of the GET path above
    url(r'^manage/requests/(?P<contact_id>\d+)/$', views.manage_requests_write, name='manage_requests_write'),
    url(r'^manage/revocations/$', views.manage_get_revocations_json, name='manage_get_revocations_json'),
    url(r'^manage/revocations/(?P<contact_id>\d+)/$', views.manage_revocations_write,
        name='manage_get_revocations_write'),
    url(r'^manage/revocations/(?P<contact_id>\d+)/undo/$', views.manage_revocations_undo,
        name='manage_get_revocations_undo'),

    url(r'^view/requests/$', views.view_active_requests, name='view_requests'),
    url(r'^view/requests/json/$', views.view_active_requests_json, name='view_requests_json'),
]

urlpatterns = [
    url(r'^standings-requests/', include(local_urlpatterns, namespace='standings-requests')),
]