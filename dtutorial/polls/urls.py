from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("lista/", views.PytanieLista.as_view(), name="lista"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:pk>/delete/", views.PytanieDelete.as_view(), name="delete"),
    path("<int:pytanie_id>/vote/", views.vote, name="vote"),
    path("create/", views.PytanieCreate.as_view(), name="create"),
    path("<int:pytanie_id>/odpowiedzi/", views.dodaj_odpowiedzi, name="odpowiedzi"),
    path('dodaj/', views.PytanieDodaj.as_view(), name='dodaj'),
]

# urlpatterns = [
#     path('', views.index, name="index"),
#     # /polls/4
#     path('<int:pytanie_id>/', views.detail, name="detail"),
#     path('<int:pytanie_id>/results/', views.results, name="results"),
#     path('<int:pytanie_id>/vote/', views.vote, name="vote"),
#     path('info/', views.info, name="info"),
# ]
