from django.db import models

from shops.models import Shop

# Create your models here.
class Status(models.Model):
    name =  models.CharField(max_length=80, unique=True, null=False, blank=False)


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    status = models.OneToOneField(Status, on_delete=models.PROTECT)

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    prev_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField(null=False, default=0)
    discount = models.PositiveIntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)