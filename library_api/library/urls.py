from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    BookListCreateView,
    BookDetailView,
    CheckoutBookView,
    ReturnBookView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('checkout/', CheckoutBookView.as_view(), name='checkout'),
    path('return/', ReturnBookView.as_view(), name='return'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
