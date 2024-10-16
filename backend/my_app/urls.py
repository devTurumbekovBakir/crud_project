from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, UserDetailViewSet, UserGroupViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'userdetails', UserDetailViewSet)
router.register(r'usergroups', UserGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
