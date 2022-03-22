from django.shortcuts import render
from api.serializer import StockSerializer, TransactionsSerializer
from rest_framework import viewsets
from .models import Stock, Transactions
# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    # This viewset automatically provides list, create, delete and retrieve actions 
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    # This viewset automatically creates CRUD actions
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer