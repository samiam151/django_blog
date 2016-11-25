from django.conf.urls import include, url
from django.contrib import admin

from .import views

urlpatterns = [
    url(r'^create$', views.post_create, name="create"),
    url(r'^$', views.post_list, name="list"), # Show all posts
    url(r'^(?P<id>\d+)$', views.post_detail, name="detail"), # Show specific post
    url(r'^(?P<id>\d+)/delete$', views.post_delete, name="delete"),
    url(r'^(?P<id>\d+)/edit$', views.post_update, name="update"), # Edit specific post
]