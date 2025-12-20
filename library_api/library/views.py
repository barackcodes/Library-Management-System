from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from django.contrib.auth.models import User
from .models import Book, Checkout
from .serializers import UserSerializer, BookSerializer, CheckoutSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = []


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class CheckoutBookView(APIView):
    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.validated_data["book"]
            book.available = False
            book.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnBookView(APIView):
    def post(self, request):
        checkout_id = request.data.get("checkout_id")

        try:
            checkout = Checkout.objects.get(id=checkout_id)
            checkout.book.available = True
            checkout.book.save()
            checkout.returned = True
            checkout.save()
            return Response({"message": "Book returned successfully"})
        except Checkout.DoesNotExist:
            return Response(
                {"error": "Checkout record not found"},
                status=status.HTTP_404_NOT_FOUND
            )
