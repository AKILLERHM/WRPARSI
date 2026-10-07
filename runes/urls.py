from django.urls import path
from . import views

urlpatterns = [

    path("runes&spells/", views.runes_ans_spells_page, name="Runes&SpellsPage"),
    path("runes/<int:pk>/detial", views.rune_detail, name="RuneDetail"),
    path("spells/<int:pk>/detial", views.spell_detail, name="SpellDetail"),
]