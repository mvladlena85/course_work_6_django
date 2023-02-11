from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from ads.models import Ad, Comment
from ads.permissions import IsAdOwnerOrAdmin, IsCommentOwnerOrAdmin
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
@extend_schema_view(
    list=extend_schema(description="Retrieve ads", summary="Ads list"),
    retrieve=extend_schema(description="Retrieve ad's detail information", summary="Advertisement"),
    create=extend_schema(description="Create advertisement", summary="Create"),
    destroy=extend_schema(description="Delete ad", summary="Delete ad"),
    update=extend_schema(description="Update ad fully", summary="Update ad"),
    partial_update=extend_schema(description="Partial update", summary="Partial update"),
    me=extend_schema(description="Retrieve ads created by current user", summary="Skills list"),
)
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()

    pagination_class = AdPagination

    default_serializer = AdDetailSerializer
    serializer_classes = {
        "list": AdSerializer,
        "me": AdSerializer,
    }

    default_permission = [AllowAny()]
    permission_classes = {
        "retrieve": [IsAuthenticated()],
        "create": [IsAuthenticated()],
        "destroy": [IsAuthenticated(), IsAdOwnerOrAdmin()],
        "update": [IsAuthenticated(), IsAdOwnerOrAdmin()],
        "partial_update": [IsAuthenticated(), IsAdOwnerOrAdmin()],
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permission_classes.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        author = self.request.user
        return serializer.save(author=author)

    @action(methods=["GET"], detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author_id=request.user.pk)
        # self.serializer_classes = AdSerializer
        return self.list(request, *args, **kwargs)


@extend_schema_view(
    list=extend_schema(description="Retrieve comments to particular ad", summary="Comments list"),
    retrieve=extend_schema(description="Retrieve comment by id", summary="Comment"),
    create=extend_schema(description="Create comment", summary="Create comment"),
    destroy=extend_schema(description="Delete comment", summary="Delete comment"),
    update=extend_schema(description="Update comment", summary="Update comment"),
    partial_update=extend_schema(description="Update comment", summary="Update comment"),
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    default_serializer = CommentSerializer
    serializer_classes = {}

    default_permission = [IsAuthenticated()]
    permission_classes = {
        "destroy": [IsAuthenticated(), IsCommentOwnerOrAdmin()],
        "update": [IsAuthenticated(), IsCommentOwnerOrAdmin()],
        "partial_update": [IsAuthenticated(), IsCommentOwnerOrAdmin()],
    }

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        return Comment.objects.filter(ad_id=ad_id)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permission_classes.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        author = self.request.user
        return serializer.save(ad_id=ad_id, author=author)
