from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'admin')


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'manager')


class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'technician')


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'client')

class AllowRoles(BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        return bool(
            request.user
            and hasattr(view, "allowed_roles")
            and request.user.role in view.allowed_roles
        )
