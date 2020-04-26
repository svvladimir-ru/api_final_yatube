from django.urls import path, include
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename="comments")
router.register('follow', FollowViewSet)
router.register('group', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
