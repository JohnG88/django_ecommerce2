from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Product(generics.RetrieveAPIView):
    # the lookup_field will pass slug to url, so don't need to use filter
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
