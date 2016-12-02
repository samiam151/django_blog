from django.conf.urls import include, url
from django.contrib import admin

from .import views
from .views import (
    PostList,
    PostDetail,
    PostCreate,
    PostUpdate,
    PostDelete
    )

urlpatterns = [
    url(r'^create$', PostCreate.as_view(), name="create"),
    url(r'^$', PostList.as_view(), name="list"), # Show all posts
    url(r'^(?P<pk>\d+)$', PostDetail.as_view(), name="detail"), # Show specific post
    url(r'^(?P<pk>\d+)/delete$', PostDelete.as_view(), name="delete"),
    url(r'^(?P<pk>\d+)/edit$', PostUpdate.as_view(), name="update"), # Edit specific post
]