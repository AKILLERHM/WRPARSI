from django.shortcuts import render
from .models import Rune, Spell



def runes_ans_spells_page(request):

    runes = Rune.objects.all()
    spells = Spell.objects.all()

    context = { "runes": runes, "spells":spells }

    return render(request, "runes/runes_and_spells_page.html", context )