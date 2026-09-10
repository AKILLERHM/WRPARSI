from django.shortcuts import render, get_object_or_404
from champions.models import Champion


def home(request):

    return render(request, "champions/home.html")


def champions_view(request):

    champs = Champion.objects.all()
    context = {"champs" : champs}

    return render(request, "champions/champions.html", context)


def champion_page(request, slug):

    champion = Champion.objects.get(slug=slug)
    context = {"champion": champion}

    return render(request, "champions/champion.html", context)