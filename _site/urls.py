from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("projekte", views.projects),
    # path("", views.main_log),
]