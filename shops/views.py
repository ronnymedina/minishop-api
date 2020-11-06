from rest_framework import viewsets

from shops.models import Shop
from shops.serializers import ShopSerializer


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer