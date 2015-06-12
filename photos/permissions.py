#encoding:UTF-8

from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Usuarios anónimos pueden crear un usuario
        Solo admins pueden ver el listado de users
        Un user solo puede ver su perfil, salvo que sea admin que ve todos
        Un user solo puede actualizar su perfil, salvo que sea admin que puede actualizar todos
        Un user solo puede borrar su perfil, salvo que sea admin que puede borrar todos

        :param request:
        :param view:
        :return:
        """
        from photos.api import UserDetailAPI

        if request.method.upper() == "POST" and not request.user.is_authenticated():
            return True

        elif request.user.is_superuser:
            return True

        elif isinstance(view, UserDetailAPI):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser