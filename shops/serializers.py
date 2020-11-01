from django.db.models import fields
from rest_framework import serializers

from shops.models import Shop


class ShopSerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ('name', 'description',)

    def create(self, request):
        print(request)

