from django.shortcuts import render
from champions.models import Champion


def home(request):

    return render(request, "champions/home.html")


def champions_view(request):

    champs = Champion.objects.all()

    context = {"champs" : champs}

    return render(request, "champions/champions.html", context)