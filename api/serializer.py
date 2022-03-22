from rest_framework import serializers
from .models import Stock, Transactions 


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'quantity', 'timestamp', 'last_modified', 'reorder_level']


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ["transaction_id", "user", "item_name", "item_id", "quantity","price", "timestamp", "type", "discount"]