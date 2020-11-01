from rest_framework import viewsets
from django.contrib.auth.models import User

from users.serializer import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
