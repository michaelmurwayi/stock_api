from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import datetime

# importing inbuilt user model
User = get_user_model()

# Transaction type choices
# This shows tool that is responsible for transaction
# Tool mean vehicle or store for this instance

TYPE_CHOICES = (
    ("STORE","STORE"),
    ("LORRY","LORRY"),
    ("PICK_UP","PICK_UP"),
    ("VAN","VAN"),
    ("WHOLESALE","WHOLESALE"),
)


# Create your models here.
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True) 
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    reorder_level = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name + ' ' + str(self.quantity) + ' ' + str(self.price)

class Transactions(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item_name = models.TextField(max_length=100)
    item_id = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    type =  models.CharField(
        max_length=20,
        choices = TYPE_CHOICES,
        default= 'STORE'
    )
    discount = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.now())