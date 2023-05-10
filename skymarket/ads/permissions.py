from rest_framework import permissions


class AdPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return request.user.is_authenticated or request.user.is_admin
        else:
            return False

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated():
            return False

        if view.action == 'retrieve':
            return obj == request.user.is_authenticated or request.user.is_admin
        elif view.action in ['update', 'partial_update', 'destroy']:
            return obj == request.user or request.user.is_admin
        else:
            return False


class CommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated or request.user.is_admin
        elif view.action == 'create':
            return request.user.is_authenticated or request.user.is_admin
        else:
            return False

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated():
            return False

        if view.action in ['update', 'partial_update', 'destroy']:
            return obj == request.user or request.user.is_admin
        else:
            return False
