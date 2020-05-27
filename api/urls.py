from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("youtube/<str:search>", views.youtubesearch, name="youtubesearch"),
]
