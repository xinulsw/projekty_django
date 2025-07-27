from django.contrib.messages import success
from django.urls import path
from . import views  # import widoków aplikacji
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Wiadomosc

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name="index"),
    path('rejestruj/', CreateView.as_view(
        template_name='czat/rejestruj.html',
        form_class=UserCreationForm,
        success_url='/'),
        name="rejestruj"),
    path('wiadomosci/', login_required(
        ListView.as_view(
            model=Wiadomosc,
            context_object_name='wiadomosci',
            paginate_by=2)),
            name='wiadomosci'),
    path('dodaj/', login_required(
        views.DodajWiadomosc.as_view(),
        login_url='/loguj'),
        name='dodaj'),
    path('<pk>/edytuj/', login_required(
        views.EdytujWiadomosc.as_view(),
        login_url='/loguj'),
        name='edytuj'),
    path('<pk>/usun/', login_required(
        DeleteView.as_view(
            model=Wiadomosc,
            template_name='czat/wiadomosc_usun.html',
            success_url='/wiadomosci'),
        login_url='/loguj'),
        name='usun'),
    path("loguj/", auth_views.LoginView.as_view(template_name="czat/loguj.html"), name='loguj'),
    path('wyloguj/', auth_views.LogoutView.as_view(), name='wyloguj'),
]
