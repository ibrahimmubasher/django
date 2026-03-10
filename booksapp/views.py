from django.shortcuts import render
from .models import Book
from .serializer import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)