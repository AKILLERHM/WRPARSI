from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,  name="Home" ),
    path("champions/", views.champions_view, name="Champions"),
    path("ChampionPage/<slug:slug>/", views.champion_page, name="ChampionPage")
]