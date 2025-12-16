from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    BookListCreateView,
    BookDetailView,
    CheckoutBookView,
    ReturnBookView
    
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    path('checkout/', CheckoutBookView.as_view(), name='checkout-book'),
    path('return/', ReturnBookView.as_view(), name='return-book'),
]