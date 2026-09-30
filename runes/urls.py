from django.urls import path
from . import views

urlpatterns = [

    path("runes&spells/", views.runes_ans_spells_page, name="Runes&SpellsPage"),

]