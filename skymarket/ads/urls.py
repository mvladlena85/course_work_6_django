from django.urls import include, path
from rest_framework_nested import routers

# TODO настройка роутов для модели

from ads.views import AdViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'ads', AdViewSet, basename='ads')

comment_router = routers.NestedSimpleRouter(router, r'ads', lookup='ad')
comment_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [

]

urlpatterns += router.urls + comment_router.urls
