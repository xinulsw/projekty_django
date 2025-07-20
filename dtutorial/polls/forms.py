from django.forms import ModelForm
from .models import Pytanie, Odpowiedz
from django.forms.models import inlineformset_factory


class PytanieForm(ModelForm):

    class Meta:
        model = Pytanie
        exclude = ('data_pub', 'autor')


OdpowiedziFormSet = inlineformset_factory(
    parent_model=Pytanie,
    model=Odpowiedz,
    max_num=6,
    min_num=1,
    validate_max=True,
    validate_min=True,
    extra=2,
    fields=('tekst_odp',)
)


class OdpowiedzForm(ModelForm):
    class Meta:
        model = Pytanie
        exclude = ('glosy',)
