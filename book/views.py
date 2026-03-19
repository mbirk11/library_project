from django.shortcuts import render, redirect
from django.views import generic
from .models import Book
from reader.models import Reader
from reader.forms import ReaderAccessForm, LoginForm

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                reader = Reader.objects.get(email=email)
                # Success! Log in
                request.session['reader_id'] = reader.id
                return redirect('reader-books')
            except Reader.DoesNotExist:
                # Not found, redirect to register with email passed in session
                request.session['temp_email'] = email
                return redirect('register')
    else:
        form = LoginForm()
            
    return render(request, 'book/index.html', {'form': form})

def register(request):
    # Try to pre-fill email from login attempt
    initial_data = {'email': request.session.get('temp_email', '')}
    
    if request.method == 'POST':
        form = ReaderAccessForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            
            reader, created = Reader.objects.get_or_create(
                email=email,
                defaults={'first_name': first_name, 'last_name': last_name, 'age': age}
            )
            request.session['reader_id'] = reader.id
            return redirect('reader-books')
    else:
        form = ReaderAccessForm(initial=initial_data)
        
    return render(request, 'book/register.html', {'form': form})

def reader_books(request):
    reader_id = request.session.get('reader_id')
    if not reader_id:
        # If accessing directly without logging in, redirect back to form
        return redirect('index')
        
    reader = Reader.objects.get(id=reader_id)
    books = Book.objects.all()
    return render(request, 'book/books_list.html', {'reader': reader, 'books': books})

# Added generic views
class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
