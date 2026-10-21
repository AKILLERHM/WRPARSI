from django.contrib import admin
from .models import (
    Champion,
    ChampionRole,
    Ability,
    Build,
    BuildItem,
    BuildBoot,
    BuildRune,
    BuildSpell,
)
from .forms import BuildItemForm, BuildBootForm, BuildRuneForm



admin.site.register(Champion)
admin.site.register(ChampionRole)
admin.site.register(Ability)


class BuildItemInline(admin.TabularInline):
    model = BuildItem
    form = BuildItemForm
    extra = 1
    fields = ("slot", "item")
    ordering = ("slot",)


class BuildBootInline(admin.TabularInline):
    model = BuildBoot
    form = BuildBootForm
    extra = 1
    fields = ("slot", "boot")
    ordering = ("slot",)


class BuildRuneInline(admin.TabularInline):
    model = BuildRune
    form = BuildRuneForm
    extra = 1
    fields = ("slot", "rune")
    ordering = ("slot",)


class BuildSpellInline(admin.TabularInline):
    model = BuildSpell
    extra = 1
    fields = ("slot", "spell")
    ordering = ("slot",)


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ("name", "champion")
    list_select_related = ("champion",)
    search_fields = ("name", "champion__name")

    inlines = [
        BuildItemInline,
        BuildBootInline,
        BuildRuneInline,
        BuildSpellInline,
    ]