#-*- coding: utf-8 -*-
__author__ = 'bibosso'

from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]




