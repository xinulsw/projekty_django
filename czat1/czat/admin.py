from django.contrib import admin
from . import models

# rejestrujemy model Wiadomosc w panelu administracyjnym
admin.site.register(models.Wiadomosc)
