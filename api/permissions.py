from rest_framework.permissions import BasePermission,DjangoModelPermissions
from django.shortcuts import get_object_or_404
from core.models import User

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS','POST')

class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        try:
            pk = view.kwargs.get('pk')
            user = get_object_or_404(User,pk=pk)
            return request.user == user
        except Exception as e:
            self.message = f"{e}"
            return False
