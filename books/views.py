from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
# Create your views here.

class BookListView(ListView):
    model : Book
    context_object_name = 'book_list' # new
    template_name = 'books/book_list.html'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
