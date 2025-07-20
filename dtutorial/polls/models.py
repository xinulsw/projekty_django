import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Pytanie(models.Model):
    tekst_pytania = models.CharField(max_length=200)
    data_pub = models.DateTimeField(
        "data publikacji",
        default=datetime.date.today)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def opublikowane_ostatnio(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.tekst_pytania


class Odpowiedz(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    tekst_odp = models.CharField(max_length=200)
    glosy = models.IntegerField(default=0)

    def __str__(self):
        return self.tekst_odp
