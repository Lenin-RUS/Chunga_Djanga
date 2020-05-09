from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated:
            return request.method in SAFE_METHODS
        return False