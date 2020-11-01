from django.urls import include, path
from rest_framework import routers

from shops.views import ShopsViewSet

router = routers.DefaultRouter()
router.register(r'', ShopsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]