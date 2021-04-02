from rest_framework import viewsets
from rest_framework.response import Response

from backend.models import Keyword, Platform
from backend.serializers import (
    UserPostSerializer,
    KeywordGetSerializer,
    PlatformGetSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    User view set for user related actions.
    Route: /users
    """

    def get_serializer_class(self):
        if self.action == "create":
            return UserPostSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response("User created.")


class KeywordViewSet(viewsets.ModelViewSet):
    """
    Keyword view set for managing keywords.
    Route: /keywords
    """

    queryset = Keyword.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return KeywordGetSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    """
    Platform view set for managing platforms.
    Route: /platforms
    """

    queryset = Platform.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PlatformGetSerializer
