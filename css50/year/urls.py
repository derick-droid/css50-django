from django.urls import path
from . import views

urlpatterns = [
    path("", views.newyear, name="newyear"),
    path("index", views.index, name="index")
]