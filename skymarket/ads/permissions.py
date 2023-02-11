# TODO здесь производится настройка пермишенов для нашего проекта

from rest_framework import permissions

from ads.models import Ad, Comment


class IsAdOwnerOrAdmin(permissions.BasePermission):
    message = "Вы не можете редактировать или удалить это сообщение"

    def has_permission(self, request, view):
        ad_id = view.kwargs.get('pk')
        ad = Ad.objects.get(pk=ad_id)
        if ad.author == request.user or request.user.role == 'admin':
            return True
        else:
            return False


class IsCommentOwnerOrAdmin(permissions.BasePermission):
    message = "Вы не можете редактировать или удалить этот комментарий"

    def has_permission(self, request, view):
        comment = Comment.objects.get(pk=view.kwargs.get('pk'))
        if comment.author == request.user or request.user.role == 'admin':
            return True
        else:
            return False
