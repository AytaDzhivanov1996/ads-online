from django.urls import include, path
from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

ad_router = routers.DefaultRouter()
ad_router.register('ads', AdViewSet, basename='ads')

comment_router = routers.DefaultRouter()
comment_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api/', include(ad_router.urls)),
    path('api/ads/<int:ad_id>/', include(comment_router.urls))
]
