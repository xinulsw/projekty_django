# Poprawki w czat2

## Plik czat2/settings.py:

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    LOGIN_REDIRECT_URL = "/"
    LOGOUT_REDIRECT_URL = "/"

## Plik czat/urls.py:

    from django.urls import reverse_lazy
    from .models import Wiadomosc

    path('rejestruj/', CreateView.as_view(
        template_name='czat/rejestruj.html',
        form_class=UserCreationForm,
        success_url='/czat/'),
        name="rejestruj"),
    path("loguj/", auth_views.LoginView.as_view(template_name="czat/loguj.html"), name='loguj'),
    path('wyloguj/', auth_views.LogoutView.as_view(), name='wyloguj'),

## Plik czat/index.html:

    {% if user.is_authenticated %}
      <p>Jesteś zalogowany jako {{ user.username }}.</p>
      <p><form action="{% url 'czat:wyloguj' %}" method="post">
           {% csrf_token %}
           <input type="submit" value="Wyloguj się">
         </form>
      </p>
    {% else %}
      <p><a href="{% url 'czat:loguj' %}">Zaloguj się</a></p>
      <p><a href="{% url 'czat:rejestruj' %}">Zarejestruj się</a></p>
    {% endif %}

## Poprawka w pliku czat/admin.py:

    from . import models

## Wstawianie linku "Wyloguj" w szablonie:

## Poprawki w pliku czat/views.py

    