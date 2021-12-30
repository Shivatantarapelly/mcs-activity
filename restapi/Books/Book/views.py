from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def book_list(request):
    book_obj = BooksModel.objects.all()
    serializer = BookSerializer(book_obj, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def post_book(request):
    book_obj = BooksModel.objects.all()
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_book(request, id):
    book_obj = BooksModel.objects.get(id=id)
    serializer = BookSerializer(instance=book_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request, id):
    book_obj = BooksModel.objects.get(id=id)
    book_obj.delete()
    return Response('Book is deleted')
