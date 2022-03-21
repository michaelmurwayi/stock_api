from django.shortcuts import render
from api.serializer import StockSerializer
from rest_framework import viewsets
from .models import Stock
# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    # This viewset automatically provides list, create, delete and retrieve actions 
    queryset = Stock.objects.all()
    serializer_class = StockSerializer