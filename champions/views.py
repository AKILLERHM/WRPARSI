from django.shortcuts import render, get_object_or_404 
from django.db.models import Q, Prefetch

from champions.models import (
    Champion, Build, BuildItem, BuildBoot, BuildRune, BuildSpell
)



def home(request):
    return render(request, "champions/home.html")


def champions_view(request):
    champs = Champion.objects.all()
    context = {"champs" : champs}
    return render(request, "champions/champions.html", context)


def champion_search(request):
    query = request.GET.get("q", "").strip()

    if query:
        champions = Champion.objects.filter(
            Q(name__icontains=query) | Q(name_parsi__icontains=query)
        )
    else:
        champions = Champion.objects.all()


    context = {"champions" : champions}
    return render(request, "partials/champion_search_results.html", context)


def champion_page(request, slug):
    champion = get_object_or_404(
        Champion.objects.prefetch_related("roles", "abilities"),
        slug=slug,
    )

    builds = (
        Build.objects.filter(champion=champion).prefetch_related(
            Prefetch("build_items", queryset=BuildItem.objects.select_related("item")),
            Prefetch("build_boots", queryset=BuildBoot.objects.select_related("boot")),
            Prefetch("build_runes", queryset=BuildRune.objects.select_related("rune")),
            Prefetch("build_spells", queryset=BuildSpell.objects.select_related("spell")),
        ).order_by("pk")
    )

    requested_build_id = request.GET.get("build")

    selected_build = (
        builds.filter(pk=requested_build_id).first()
        if requested_build_id
        else builds.first()
    )

    build_slots = None

    if selected_build:
        items = {
            obj.slot: obj.item
            for obj in selected_build.build_items.all()
        }
        boots = {
            obj.slot: obj.boot
            for obj in selected_build.build_boots.all()
        }
        runes = {
            obj.slot: obj.rune
            for obj in selected_build.build_runes.all()
        }
        spells = {
            obj.slot: obj.spell
            for obj in selected_build.build_spells.all()
        }


        build_slots = {
            "items": [items.get(slot) for slot in range(1, 6)],
            "boots": [boots.get(slot) for slot in range(1, 3)],
            "runes": [runes.get(slot) for slot in range(1, 6)],
            "spells": [spells.get(slot) for slot in range(1, 3)],
        }

    context = {"champion": champion,
               "builds": builds,
               "selected_build": selected_build,
               "build_slots": build_slots}
    return render(request, "champions/champion.html", context)