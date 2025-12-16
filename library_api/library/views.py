from django_filters.rest_framework  import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import generics

from .models import User, Book
from .serializers import UserSerializer, BookSerializer


from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework  import status
from django.utils  import timezone
from rest_framework.permissions import IsAuthenticated

from .models import Book, Checkout
from .serializers  import CheckoutSerializer


class CheckoutBookView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        
        if serializer.is_valid():
            checkout = serializer.save()
            
            book = checkout.book
            book.available = False
            book.save()
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReturnBookView(APIView):
    def post(self, request):
        checkout_id = request.data.get("checkout_id")
        
        try:
            checkout = Checkout.objects.get(id=checkout_id, returned=False)
        except Checkout.DoesNotExist:
            return Response(
                {
                    "error": "Invalid checkout ID or book already returned."},
                    status=status.HTTP_400_BAD_REQUEST
                
            )
            
        checkout.returned = True
        checkout.return_date = timezone.now()
        checkout.save()
        
        book = checkout.book
        book.available = True
        book.save()
        
        
        return Response({"message": "Book returned successfully."})

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']