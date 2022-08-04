from rest_framework import permissions


class IsAuthenticatedOrStaff(permissions.BasePermission):
    """Custom permission: authenticated users can view, staff can edit."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        else:
            return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        else:
            return request.user.is_staff
