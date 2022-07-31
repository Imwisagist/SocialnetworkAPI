from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Пермишен ограничивающий действия до безопасных если не автор"""
    message = 'Нельзя)'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
