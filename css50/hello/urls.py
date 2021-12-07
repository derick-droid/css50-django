from django.urls import path
from . import views

urlpatterns =[
    path("derrick", views.derick, name="derrick"),
    path("enock", views.enock, name="enock"),
    path("greet", views.greet, name = "greet"),
    path("first", views.first, name = "first"),
    path("", views.greet, name = "greet"),
    path("<str:name>", views.html_greet, name = "html_greet"),
    path("<str:name>", views.all_greet, name = "all_greet"),
    
]