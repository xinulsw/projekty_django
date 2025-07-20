from django.urls import path
from . import views

app_name = "czat"
urlpatterns = [
    path("", views.index, name="index"),
    path("loguj/", views.loguj, name="loguj"),
    path("wyloguj/", views.wyloguj, name="wyloguj"),
    path("wiadomosci/", views.wiadomosci, name="wiadomosci"),
]