from django.shortcuts import render, get_object_or_404
from .models import Rune, Spell



def runes_ans_spells_page(request):

    primary_runes = Rune.objects.filter(role=Rune.Role.PRIMARY)

    #ترتیب نمایش ستون های رون های فرعی
    category_order = [
        (Rune.SecondaryCategory.DOMINATION, "Domination"),
        (Rune.SecondaryCategory.PRECISION, "Precision"),
        (Rune.SecondaryCategory.RESOLVE, "Resolve"),
        (Rune.SecondaryCategory.SORCERY, "sorcery"),
    ]

    secondary_groups = [
        {
            "code": code,
            "label": label,
            "runes": Rune.objects.filter(
                role=Rune.Role.SECONDARY,
                secondary_category=code,
            ),
        }
        for code,label in category_order
    ]

    spells = Spell.objects.all()

    context = {
        "primary_runes": primary_runes,
        "secondary_groups": secondary_groups,
        "spells": spells
    }

    return render(request, "runes/runes_and_spells_page.html", context )



def rune_detail(request, pk):
    rune = get_object_or_404(Rune, pk=pk)
    return render(request, "partials/rune_detail.html", {"rune": rune})



def spell_detail(request, pk):
    spell = get_object_or_404(Spell, pk=pk)
    return render(request, "partials/spell_detail.html", {"spell": spell})