from rest_framework.permissions import BasePermission

from authentication.models import User


class CategoryCreatePermission(BasePermission):
    massage = "Adding category for not MODERATOR user not allowed"

    def has_permission(self, request, view):
        if request.user.role == User.Role.MODERATOR:
            return True
        else:
            return False
