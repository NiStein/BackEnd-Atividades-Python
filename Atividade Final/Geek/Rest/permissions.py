from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status

class UserPermissions(BasePermission):
    message = 'Apenas para membros'

    def has_permission(self, request, view):
        
        user = request.user
        print(user.message)
        if 'membro' not in user.username:
            return False
        
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        
        return super().has_object_permission(request, view, obj)