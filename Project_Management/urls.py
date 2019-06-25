from django.conf.urls import url
from . import views

app_name = 'Project_Management'
urlpatterns = [
    url(r'^welding_task/$', views.welding_task,name='welding_task'),
    url(r'^create_weldingtask/$', views.create_weldingtask,name='create_weldingtask'),
    url(r'^delete_weldingtask/$', views.delete_weldingtask,name='delete_weldingtask'),
    url(r'^welding_task_detail/(?P<ID>[\w\-]+)/$', views.welding_task_detail,name='welding_task_detail'),
    url(r'^monitor/(?P<ID>[\w\-]+)/$', views.monitor,name='monitor'),
    url(r'^edit_welding_task/(?P<ID>[\w\-]+)/$', views.edit_welding_task,name='edit_welding_task'),
    url(r'^refresh_current/(?P<ID>[\w\-]+)/$', views.refresh_current, name='refresh_current'),
    url(r'^refresh_voltage/(?P<ID>[\w\-]+)/$', views.refresh_voltage, name='refresh_voltage'),
    url(r'^refresh_sound/(?P<ID>[\w\-]+)/$', views.refresh_sound, name='refresh_sound'),
    url(r'^refresh_robot/(?P<ID>[\w\-]+)/$', views.refresh_robot, name='refresh_robot'),
    #url(r'^refresh_weldpool/(?P<ID>[\w\-]+)/$', views.refresh_weldpool, name='refresh_weldpool'),
    url(r'^refresh_current/(?P<ID>[\w\-]+)/summary/$', views.refresh_current_summary, name='refresh_current_summary'),
    url(r'^refresh_voltage/(?P<ID>[\w\-]+)/summary/$', views.refresh_voltage_summary, name='refresh_voltage_summary'),
    url(r'^refresh_sound/(?P<ID>[\w\-]+)/summary/$', views.refresh_sound_summary, name='refresh_sound_summary'),
    url(r'^refresh_weldpool/(?P<ID>[\w\-]+)/summary/$', views.refresh_weldpool_summary, name='refresh_weldpool_summary'),
    url(r'^(?P<ID>[\w\-]+)/sound/$', views.sound, name='sound'),
    url(r'^(?P<ID>[\w\-]+)/current_voltage/$', views.current_voltage, name='current_voltage'),
    url(r'^(?P<ID>[\w\-]+)/weldpool/$', views.weldpool, name='weldpool'),
    url(r'^(?P<ID>[\w\-]+)/intro/$', views.intro, name='intro'),
    url(r'^(?P<ID>[\w\-]+)/mon/$', views.mon, name='mon'),
    url(r'^(?P<ID>[\w\-]+)/equip/$', views.equip, name='equip'),
    url(r'^(?P<ID>[\w\-]+)/robot/$', views.robot, name='robot'),
    url(r'^(?P<ID>[\w\-]+)/spectrum/$', views.spectrum, name='spectrum'),
    url(r'^(?P<ID>[\w\-]+)/refresh_monitor/$', views.refresh_monitor, name='refresh_monitor'),
]