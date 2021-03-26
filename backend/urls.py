from django.http import HttpResponse
from django.urls import path


urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
]
