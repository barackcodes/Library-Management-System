from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Checkout

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
        
    def validate(self, data):
        book = data["book"]
        if not book.available:
            raise serializers.ValidationError("This book is not available.")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
