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
        return Response("User created.", status=201)


class KeywordViewSet(viewsets.ModelViewSet):
    """
    Keyword view set for managing keywords.
    Route: /keywords
    """

    def get_queryset(self):
        queryset = Keyword.objects.all()

        # Filter by phrase.
        phrase = self.request.GET.get("phrase")
        if phrase is not None:
            for term in phrase.split():
                queryset = queryset.filter(name__icontains=term)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return KeywordGetSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    """
    Platform view set for managing platforms.
    Route: /platforms
    """

    def get_queryset(self):
        queryset = Platform.objects.all()

        # Filter by phrase.
        phrase = self.request.GET.get("phrase")
        if phrase is not None:
            for term in phrase.split():
                queryset = queryset.filter(name__icontains=term)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return PlatformGetSerializer
