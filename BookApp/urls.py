from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mainmenu),
    path('book-list/', book_list, name='book-list'),
    path('book-create/', book_create, name='book-create'),
    path('book-update/<int:id>/', book_update, name='book-update'),
    path('book-delete/<int:id>/', book_delete, name='book-delete'),
    path('book-detail/<int:id>/', book_detail, name='book-detail'),
]
