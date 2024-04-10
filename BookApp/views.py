from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def mainmenu(request):
    return render(request,'base.html', context={})

def base_view(request):
    return render(request, 'base.html', context={})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book-list.html', context={'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # model = form.instance
            return redirect('book-list')
    else:
        form = BookForm()

    return render(request, 'book-create.html', context={'form': form})

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance = book)
    # if request.method == 'POST':
    #     form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        # model = form.instance
        return redirect('book-list')


    return render(request, 'book-update.html', context={'form': form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book-list')

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book-detail.html', context={'book': book})





# Create your views here.
