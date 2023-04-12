from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostView, GroupView, CommentView, FollowView

router = SimpleRouter()
router.register('posts', PostView)
router.register('groups', GroupView)
router.register('follow', FollowView)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentView)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
