# from socket import fromshare
from django import forms
from books.models import Book

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        