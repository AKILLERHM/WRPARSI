from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,  name="Home" ),
    path("champions/", views.champions_view, name="Champions"),
    path("search/", views.champion_search, name="ChampionSearch"),
    path("ChampionPage/<slug:slug>/", views.champion_page, name="ChampionPage"),
]