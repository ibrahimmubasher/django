from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer

class BookListView(APIView):

    def get(self, request):
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class AuthorListView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):

    def get(self, request, pk):
        author_obj = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        author_obj = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author_obj = get_object_or_404(Author, pk=pk)
        author_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)