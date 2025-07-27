from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from django.views.generic import CreateView

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('rejestruj/', CreateView.as_view(
        template_name='users/rejestruj_form.html',
        form_class=UserCreationForm,
        success_url='/'),
        name="rejestruj"),
]
