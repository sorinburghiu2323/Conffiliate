from django.urls import path
from . import views

app_name = "affiliate_mvp"

urlpatterns = [
    path('', views.index, name="index"),
]
