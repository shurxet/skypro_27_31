from rest_framework.permissions import BasePermission

from ads.models import Selection, Ad
from authentication.models import User


class CategoryCreatePermission(BasePermission):
    massage = "Adding category for not MODERATOR user not allowed"

    def has_permission(self, request, view):
        if request.user.role == User.Role.MODERATOR:
            return True
        else:
            return False


class SelectionUpdatePermission(BasePermission):
    massage = "Editing is prohibited for non-owners of the collection"

    def has_permission(self, request, view):
        try:
            selection = Selection.objects.get(pk=view.kwargs["pk"])
        except Selection.DoesNotExist:
            return False

        if selection.owner.id == request.user.id:
            return True
        elif request.user.role != User.Role.MEMBER:
            return True
        else:
            return False


class AdUpdatePermission(BasePermission):
    massage = "Editing is prohibited for non-owners of the collection"

    def has_permission(self, request, view):
        try:
            ad = Ad.objects.get(pk=view.kwargs["pk"])
        except Selection.DoesNotExist:
            return False

        if ad.author.id == request.user.id:
            return True
        elif request.user.role != User.Role.MEMBER:
            return True
        else:
            return False
