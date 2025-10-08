from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer,UserSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializer
    def create(self,request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.usr
