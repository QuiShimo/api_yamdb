from rest_framework import permissions


class IsAdminOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or (request.user.is_authenticated
                                     and request.user.is_admin):
            return True

