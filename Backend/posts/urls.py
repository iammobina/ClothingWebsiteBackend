from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    post_create,
    post_detail,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]
