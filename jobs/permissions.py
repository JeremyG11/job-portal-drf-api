from rest_framework import permissions

class JobPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True
    
    def has_object_permission(self, request, view, object):

        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE.METHODS:
            return True

        if object.posted_by == request.user:
            return True
            
        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False