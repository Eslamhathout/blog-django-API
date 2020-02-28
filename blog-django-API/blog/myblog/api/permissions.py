from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # It means that the request is GET of HEAD or any other safe methods other than update or delete
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author