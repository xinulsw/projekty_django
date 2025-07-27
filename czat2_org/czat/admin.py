from django.contrib import admin
from . import models  # importujemy nasz model

# rejestrujemy model Wiadomosc w panelu administracyjnym
admin.site.register(models.Wiadomosc)
