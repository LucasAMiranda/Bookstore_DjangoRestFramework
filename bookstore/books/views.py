from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer


class BookCollection(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

