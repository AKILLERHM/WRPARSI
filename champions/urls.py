from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,  name="Home" ),
    path("champions/", views.champions_view, name="champions"),
    path("ChampionPage/<int:pk>/", views.champion_page, name="ChampionPage")
]