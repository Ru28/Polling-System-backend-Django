from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet, VoteViewSet, CommentViewSet, UserProfileViewSet, UserViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
