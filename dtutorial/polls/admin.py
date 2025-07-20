from django.contrib import admin

from .models import Pytanie, Odpowiedz
# Register your models here.

admin.site.register(Pytanie)
admin.site.register(Odpowiedz)
