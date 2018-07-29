#!/usr/bin/env python3
from django.urls import path
import views
urlpatterns=[
    path('books/<int:year>',views.book_archive),
]