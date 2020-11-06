from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, null=False, unique=True)
    description = models.TextField(max_length=600, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Tag(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, null=False)
