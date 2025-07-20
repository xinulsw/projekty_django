## Poprawka w klasie Wiadomosc (czat/models.py):

autor = models.ForeignKey(User, on_delete=models.CASCADE)

## Poprawka w pliku czat/admin.py:

from . import models

## Poprawki w pliku czat/urls.py:

from django.urls import path

path("", views.index, name="index")
