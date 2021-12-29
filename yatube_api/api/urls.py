from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewset

app_name = 'api'

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewset, basename='Comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
