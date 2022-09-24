from django.shortcuts import render
from books.models import Book
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.forms import BookModelForm
# Create your views here.


#To get all books

def BooksIndex(request):
    allb = Book.get_all_books()
    return render(request, "books/index.html", context={"books":allb})


class BookDetails(DetailView):
    model = Book
    template_name = "books/show.html"


class CreateBookView(CreateView):
    template_name = "books/create.html"
    form_class = BookModelForm
    success_url = '/books/index'

class EditBookView(UpdateView):
    model = Book
    template_name = "books/edit.html"
    success_url = '/books/index'
    form_class = BookModelForm

class DeleteBookView(DeleteView):
    model = Book
    template_name = "books/delete.html"
    success_url = '/books/index'
    # form_class = BookModelForm