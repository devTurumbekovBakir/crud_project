from rest_framework import viewsets
from .models import UserProfile, UserDetail, UserGroup
from .serializers import UserProfileSerializer, UserDetailSerializer, UserGroupSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "user_notifications",
            {
                "type": "notify_user_creation",
                "message": f"User {user.username} has been created.",
            }
        )


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
