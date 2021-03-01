from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls import url

app_name = 'music'

urlpatterns = [
    # it will match to /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # registration link
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # it will match to /music/71/  some album id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$' , views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete$' , views.AlbumDelete.as_view(), name='album-delete'),
]

