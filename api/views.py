from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import UserCreateSerializer,UserSerializer
from core.models import User
from .permissions import UserPermission

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = (UserSerializer,)
    permission_classes = (permissions.IsAuthenticated)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


    def get_permissions(self):
        if self.action == 'create' or self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny(),]
        return [permissions.IsAuthenticated(),UserPermission(),]


    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer