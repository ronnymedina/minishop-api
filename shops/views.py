from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from shops.models import Shop

from shops.serializers import ShopSerializer


class ShopsViewSet(viewsets.ViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticated,)
