from django.contrib import admin
from .models import Champion, ChampionRole, Ability


admin.site.register(Champion)
admin.site.register(ChampionRole)
admin.site.register(Ability)