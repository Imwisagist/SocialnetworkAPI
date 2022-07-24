from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    PostViewSet,
    GroupViewSet,
    FollowViewSet,
    CommentViewSet
)

router = DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet, basename='group')
router.register('posts', PostViewSet, basename='post')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
]
