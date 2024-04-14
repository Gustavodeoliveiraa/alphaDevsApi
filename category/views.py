from rest_framework import generics
from category.models import Category
from category.serializer import CategorySerializer

class CreateListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RetrieveUpdateDestroyTag(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer