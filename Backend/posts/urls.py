from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
]
