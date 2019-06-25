from django.conf.urls import url
from . import views

app_name = 'INDEX'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'exit/$', views.exit, name='exit'),
]