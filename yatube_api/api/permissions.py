from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешает доступ (изменение/удаление) только пользователю-автору."""
    message = ''

    def has_permission(self, request, view):
        self.message = 'Необходима авторизация.'
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        self.message = 'Необходимо авторство.'
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
