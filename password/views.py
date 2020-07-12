from rest_framework import generics

from .models import Password
from .serializers import PasswordSerializer

class PasswordList(generics.ListCreateAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer


