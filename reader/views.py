from django.shortcuts import render, redirect, get_object_or_404
from .models import Reader
from book.models import Book

def profile_view(request):
    reader_id = request.session.get('reader_id')
    if not reader_id:
        return redirect('index')
    
    reader = get_object_or_404(Reader, id=reader_id)
    my_books = reader.books.all()
    
    return render(request, 'reader/profile.html', {
        'reader': reader,
        'my_books': my_books
    })

def add_to_profile(request, book_id):
    reader_id = request.session.get('reader_id')
    if not reader_id:
        return redirect('index')
    
    reader = get_object_or_404(Reader, id=reader_id)
    book = get_object_or_404(Book, id=book_id)
    
    reader.books.add(book)
    return redirect('reader_profile')
