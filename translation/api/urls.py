from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RequesterViewSet

router = DefaultRouter()
router.register('requesters', RequesterViewSet, basename='requesters')
# router.register('posts', PostViewSet, basename='posts')
# router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
#                 basename='comments')
# router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
