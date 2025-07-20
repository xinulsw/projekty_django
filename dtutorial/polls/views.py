from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.db.models import F
from . models import Pytanie, Odpowiedz
from .forms import PytanieForm, OdpowiedziFormSet
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.forms.models import modelformset_factory


def index(request):
    return render(request, "polls/index.html")

class PytanieLista(generic.ListView):
    def get_queryset(self):
        """Return the last five published questions."""
        return Pytanie.objects.order_by("-data_pub")[:5]

class DetailView(generic.DetailView):
    model = Pytanie
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Pytanie
    template_name = "polls/results.html"

def vote(request, question_id):
    pytanie = get_object_or_404(Pytanie, pk=question_id)
    try:
        odp = pytanie.odpowiedz_set.get(pk=request.POST["odpowiedz"])
    except (KeyError, Odpowiedz.DoesNotExist):
        return render(request, "polls/detail.html",
                      {"pytanie": pytanie, "error_message": "Nie wybrałeś odpowiedzi!"}
                      )

    odp.glosy = F("glosy") + 1
    odp.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

class PytanieDelete(generic.DeleteView):
    model = Pytanie
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls:index")


@method_decorator(login_required, 'dispatch')
class PytanieCreate(generic.CreateView):
    model = Pytanie
    fields = ["tekst_pytania"]
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

@login_required
def dodaj_odpowiedzi(request, pytanie_id):
    try:
        pytanie = get_object_or_404(Pytanie, pk=pytanie_id)
    except Pytanie.DoesNotExist:
        raise Http404("Pytanie nie istnieje!")
    OdpowiedziFormSet = modelformset_factory(Odpowiedz, fields=["tekst_odp"], min_num=1, max_num=5, extra=2, validate_max=True)
    queryset = Odpowiedz.objects.filter(pytanie=pytanie)
    if request.method == "POST":
        formset = OdpowiedziFormSet(
            request.POST,
            queryset=queryset
        )
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = OdpowiedziFormSet(queryset=queryset)
    return render(request, "polls/odpowiedzi_form.html", {"pytanie": pytanie, "formset": formset})

@method_decorator(login_required, 'dispatch')
class PytanieDodaj(generic.CreateView):
    """Widok dodawania pytania i odpowiedzi."""

    model = Pytanie
    form_class = PytanieForm
    success_url = reverse_lazy('polls:lista')
    template_name = 'polls/pytanie_dodaj.html'

    def get_context_data(self, **kwargs):
        context = super(PytanieDodaj, self).get_context_data(**kwargs)
        if self.request.POST:
            context['odpowiedzi'] = OdpowiedziFormSet(self.request.POST)
        else:
            context['odpowiedzi'] = OdpowiedziFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        odpowiedzi = OdpowiedziFormSet(self.request.POST)
        if form.is_valid() and odpowiedzi.is_valid():
            return self.form_valid(form, odpowiedzi)
        else:
            return self.form_invalid(form, odpowiedzi)

    def form_valid(self, form, odpowiedzi):
        form.instance.autor = self.request.user
        self.object = form.save()
        odpowiedzi.instance = self.object
        odpowiedzi.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, odpowiedzi):
        return self.render_to_response(
            self.get_context_data(form=form, odpowiedzi=odpowiedzi)
        )

# def index(request):
#     latest_question = Pytanie.objects.order_by("-data_pub")[:5]
#     print(latest_question)
#     context = {
#         "latest_question": latest_question,
#     }
#     return render(request, "polls/index.html", context)

# def detail(request, pytanie_id):
#     try:
#         pytanie = get_object_or_404(Pytanie, pk=pytanie_id)
#     except Pytanie.DoesNotExist:
#         raise Http404("Pytanie nie istnieje!")
#     return render(request, "polls/detail.html", {"pytanie": pytanie})

# def results(request, pytanie_id):
#     pytanie = get_object_or_404(Pytanie, pk=pytanie_id)
#     return render(request, "polls/results.html", {"pytanie": pytanie})

# def info(request):
#     return HttpResponse("<h1>Informacje</h1><p>To bardzo ważne informacje</p>")
