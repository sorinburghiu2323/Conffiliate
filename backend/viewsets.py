from rest_framework import viewsets
from rest_framework.response import Response

from backend.serializers import UserPostSerializer


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
