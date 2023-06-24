from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from django.shortcuts import redirect
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        Book.objects.create(title=title, author=author, description=description)
        return redirect('book_list')
    return render(request, 'bookstore/add_book.html')

def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    # Add code to add book to the shopping cart
    return redirect('book_list')
