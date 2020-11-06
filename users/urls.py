from rest_framework import routers
from django.urls import include, path

from users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls
