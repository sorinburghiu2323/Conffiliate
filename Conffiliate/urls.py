from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

vue_urls = [
    re_path(
        r"^(?:.*/|)",
        lambda request: HttpResponse(render(request, "vue_index.html")),
    ),
]

urlpatterns = [
    path("demo", include("affiliate_mvp.urls")),
    path("api/", include("backend.urls")),
    path("admin/", admin.site.urls),
    path("", include(vue_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
