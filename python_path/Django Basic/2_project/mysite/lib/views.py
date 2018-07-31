from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    return HttpResponse("Hello,World!")

def detail(request):
    book_list=Book.objects.order_by('-pub_date')[:5]
    context={'book_list':book_list}
    return render(request,'lib/detail.html',context=context)
    