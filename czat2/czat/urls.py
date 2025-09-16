from django.urls import path
from . import views  # import widoków aplikacji
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from .models import Wiadomosc

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', login_required(
        ListView.as_view(
            model=Wiadomosc,
            context_object_name='wiadomosci',
            paginate_by=2)),
        name='lista'),
    path('dodaj/', login_required(
        views.DodajWiadomosc.as_view()),
        name='dodaj'),
    path('edytuj/<pk>', login_required(
        views.EdytujWiadomosc.as_view()),
        name='edytuj'),
    path('usun/<pk>', login_required(
        DeleteView.as_view(
            model=Wiadomosc,
            template_name='czat/wiadomosc_usun.html',
            success_url='/wiadomosci')),
        name='usun'),
]
