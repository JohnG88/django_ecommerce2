from django.shortcuts import render
from rest_framework import generics
# if get no model has no objects, just write line below, then write line in get_queryset
from . import models
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
    
class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        # gets slug from url api/category/<slug:slug>/
        return models.Product.objects.filter(category__slug=self.kwargs['slug'])
