from django.http import HttpResponse
from django.urls import path
from rest_framework import routers

from backend.viewsets import *

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
] + router.urls
