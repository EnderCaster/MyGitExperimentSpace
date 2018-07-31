#!/usr/bin/env python3
# -*- utf8 -*-
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('detail/',views.detail,name='detail')
]