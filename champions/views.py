from django.shortcuts import render, get_object_or_404
from champions.models import Champion , Item, ItemType
from django.db.models import Q


def home(request):

    return render(request, "champions/home.html")


def champions_view(request):

    champs = Champion.objects.all()
    context = {"champs" : champs}

    return render(request, "champions/champions.html", context)


def champion_search(request):
    query = request.GET.get("q", "").strip()

    if not query:
        champions = Champion.objects.all()
    else:
        champions = Champion.objects.filter(
            Q(name__icontains=query) |
            Q(name_parsi__icontains=query)
        )

    context = {"champions" : champions}

    return render(request, "partials/champion_search_results.html", context)


def champion_page(request, slug):

    champion = Champion.objects.get(slug=slug)
    context = {"champion": champion}

    return render(request, "champions/champion.html", context)


def items_page(request):

    item_types = ItemType.objects.prefetch_related("items").all()
    context = {"item_types": item_types}

    return render(request, "champions/items.html", context)


def item_search(request):

    query = request.GET.get("q", "").strip()

    if not query:
        items = Item.objects.all()
    else:
        items = Item.objects.filter(
        Q(name__icontains=query)
        )
    context = {"items": items}

    return render(request, "partials/item_search_results.html", context)


def item_page(request, slug):

    item = get_object_or_404(Item, slug=slug)
    context = {"item": item}

    return render(request, "partials/item_page.html", context)