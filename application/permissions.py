from rest_framework import permissions

class isApplicationOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view, object):
        if object.applicant  == request.user:
            return True
        return False

