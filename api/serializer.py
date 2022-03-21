from rest_framework import serializers
from .models import Stock 


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'quantity', 'timestamp', 'last_modified', 'reorder_level']