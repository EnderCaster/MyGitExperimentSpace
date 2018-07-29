#!/usr/bin/env python3
# -*- utf8 -*-

from django.db import models
class book(models.Model):
    name=models.CharField(max_length=100)
    pub_date=models.DateField()

class Person(models.Model):
    pass