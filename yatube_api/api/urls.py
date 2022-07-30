from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    PostViewSet,
    GroupViewSet,
    FollowViewSet,
    CommentViewSet
)

router_v1 = DefaultRouter()
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),

]
