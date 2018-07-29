#!/usr/bin/env python3
# -*- utf8 -*-
from django.shortcuts import render
from models import Person

def book_archive(request,year):
    book_list=Person.objects.filter(birth_year=year)
    context={"year":year,'book_list':book_list}
    return render(request,'books/year_archive.html',context)
