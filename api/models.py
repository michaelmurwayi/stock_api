from django.db import models
from django.conf import settings
from django.utils import timezone

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
