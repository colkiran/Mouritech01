from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSrializer

class ProductList(APIView):

    def get(self, request):
        prod = Product.objects.all()
        serializer = ProductSrializer(prod, many=True)
        return Response(serializer.data)
