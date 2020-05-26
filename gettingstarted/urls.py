from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]
