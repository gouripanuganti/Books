from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book
from django.http import Http404


def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books': all_books
    }
    return render(request,'books/index.html',context)

def detail(request,book_id):
    try:
        book  = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This is not exist')
    return render(request,'books/detail.html',{'book':book})
