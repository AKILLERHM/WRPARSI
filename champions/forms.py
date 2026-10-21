from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import ModelChoiceIterator

from items.models import Item, ItemType
from runes.models import Rune
from .models import BuildItem, BuildBoot, BuildRune


ITEM_CODES = (
    ItemType.Code.FIGHTER,
    ItemType.Code.ASSASSIN,
    ItemType.Code.MARKSMAN,
    ItemType.Code.MAGIC,
    ItemType.Code.DEFENSE,
    ItemType.Code.SUPPORT,
)

BOOT_CODES = (
    ItemType.Code.BOOT2,
    ItemType.Code.BOOT3,
)


class GroupedItemIterator(ModelChoiceIterator):
    def __iter__(self):
        groups = defaultdict(list)

        for item in self.queryset:
            for item_type in item.type.all():
                if item_type.code in ITEM_CODES:
                    groups[item_type.get_code_display()].append(
                        self.choice(item)
                    )

        for group_name in sorted(groups):
            yield (group_name, groups[group_name])



class GroupedItemField(forms.ModelChoiceField):
    iterator = GroupedItemIterator


class BuildItemForm(forms.ModelForm):
    item = GroupedItemField(
        queryset=Item.objects.none(),
        label="Item",
        empty_label="Choose an item"
    )

    class Meta:
        model = BuildItem
        fields = ("item", "slot")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["item"].queryset = (
            Item.objects.filter(type__code__in=ITEM_CODES)
            .distinct()
            .prefetch_related("type")
            .order_by("name")
        )

    def clean_slot(self):
        slot = self.cleaned_data["slot"]
        if not 1 <= slot <= 5:
            raise ValidationError("Item slot must be between 1 and 5.")
        return slot


class BuildBootForm(forms.ModelForm):
    boot = forms.ModelChoiceField(
        queryset=Item.objects.filter(type__code__in=BOOT_CODES).distinct(),
        label="Boot",
        empty_label="Choose a boot",
    )

    class Meta:
        model = BuildBoot
        fields = ("slot", "boot")

    def clean(self):
        cleaned_data = super().clean()
        slot = cleaned_data.get("slot")
        boot = cleaned_data.get("boot")

        if slot not in (1, 2) or not boot:
            return cleaned_data


        boot_codes = set(boot.type.values_list("code", flat=True))

        if slot == 1 and ItemType.Code.BOOT2 not in boot_codes:
            self.add_error("boot", "Slot 1 requires an upgraded boot.")

        if slot == 2 and ItemType.Code.BOOT3 not in boot_codes:
            self.add_error("boot", "Slot 2 requires an upgraded boot.")

        return cleaned_data



class BuildRuneForm(forms.ModelForm):
    class Meta:
        model = BuildRune
        fields = ("slot", "rune")

    def clean(self):
        cleaned_data = super().clean()
        slot = cleaned_data.get("slot")
        rune = cleaned_data.get("rune")

        if slot not in (1, 2, 3, 4, 5) or not rune:
            return cleaned_data

        if slot == 1 and rune.role != Rune.Role.PRIMARY:
            self.add_error("rune", "slot 1 requires a primary rune.")

        if slot in (2, 3, 4, 5) and rune.role != Rune.Role.SECONDARY:
            self.add_error("rune", "Slots 2-5 require secondary runes.")

        return cleaned_data