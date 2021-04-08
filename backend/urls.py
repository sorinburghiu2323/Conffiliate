from django.http import HttpResponse
from django.urls import path
from rest_framework import routers

from backend.viewsets import *

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"keywords", KeywordViewSet, basename="keywords")
router.register(r"platforms", PlatformViewSet, basename="platforms")

urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
] + router.urls
