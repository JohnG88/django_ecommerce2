from django.shortcuts import render
from rest_framework import generics
# if get no model has no objects, just write line below, then write line in get_queryset
from . import models
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
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
        '''
          Men = level=0
            Clothes = level=1
            shoes = level=1
              Boots = level=2
        '''
        # This line wil get everything in clothes and its children, shoes and its children
        return models.Product.objects.filter(category__in=Category.objects.get(slug=self.kwargs['slug']).get_descendants(include_self=True))
    # check in admin categories

class CategoryListView(generics.ListAPIView):
    # This filters the hierarchy in categories
    '''
      Men = level=0
        Clothes = level=1
        shoes = level=1
          Boots = level=2
    '''
    # check in admin categories
    queryset = Category.objects.filter(level=1)
    serializer_class = CategorySerializer
