from django.contrib import admin
from .models import Champion, ChampionRole, Ability, Item, ItemType, ItemBuildPath


admin.site.register(Champion)
admin.site.register(ChampionRole)
admin.site.register(Ability)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(ItemBuildPath)