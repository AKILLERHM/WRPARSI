from django.db import models
from django.utils.text import slugify
from items.models import Item
from runes.models import Rune, Spell



class ChampionRole(models.Model):
    #هر چمپی برای خود لین های مخصوصی دراد...چون ممکن است چمپی چند لین داشته
    #باشد از این روش استفاده شده
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=64)
    icon_url = models.URLField(blank=True, null=True)

    class Meta:
             verbose_name = "Role"
             verbose_name_plural = "Roles"

    def __str__(self):
             return self.name



class Champion(models.Model):

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    #اگر زمانی نامی ساختیم بطور خودکار حالت slug ان دخیره میشود.
    #از slug برای جستجو کردن دقیق تر و نمایش بهتر لینک قهرمان ها استفاده می کنیم.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    name_parsi = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    title_parsi = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True, null=True)
    picture_url = models.URLField(blank=True, null=True)

    #هر چمپی ممکن است در لین های متفاوتی بازی کند
    # از این مدل برای روابط بین چمپ و لین استفاده کردم 
    roles = models.ManyToManyField(ChampionRole, related_name="champions")

    class Meta:
         ordering = ["name"]

    def __str__(self):
        return self.name



class Ability(models.Model):

    """ به این دلیل که نوع و منبع توانایی ها خاص هستند، یعنی اینکه تنها 
    یک مقدار دارند یا مقداری ندارند، بنابراین از یک حالت انتخابی استفاده شده است"""
    class AbilityType(models.TextChoices):

        PASSIVE = "passive", "Passive"
        FIRST =  "first", "First Ability"
        SECOND = "second", "Second Ability"
        THIRD = "third", "Third Ability"
        ULTIMATE = "ultimate", "Ultimate"

    class ResourceType(models.TextChoices):

         MANA = "mana", "Mana"
         ENERGY = "energy", "Energy"
         HEALTH = "health", "Health"
         NONE = "none", "None"

    """ هر توانایی بطور خاص به چمپ مورد نظرش وصل شده 
    و اگر زمانی چمپی حدف شود، توانایی های مربوط به آن هم حذف خواهد شد"""
    champion = models.ForeignKey(Champion,
                                 on_delete=models.CASCADE,
                                 related_name="abilities")

    type = models.CharField(max_length=32,
                            choices=AbilityType.choices)

    name = models.CharField(max_length=128)
    picture = models.URLField(blank=True)
    video = models.URLField(blank=True)
    cost = models.CharField(max_length=128, blank=True)
    cooldown = models.CharField(max_length=128, blank=True)
    description = models.TextField()

    resource_type = models.CharField(max_length=32,
                                     choices=ResourceType.choices)

    def __str__(self):
        return f"{self.champion} --- {self.type} ---{self.name}"



class Build(models.Model):
    champion = models.ForeignKey(
        Champion,
        on_delete=models.CASCADE,
        related_name="builds"
    )
    name = models.CharField(max_length=128)

    def __str__(self):
         return f"{self.champion.name} - {self.name}"



class BuildItem(models.Model):
    build = models.ForeignKey(
        Build,
        on_delete=models.CASCADE,
        related_name="build_items"
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    slot = models.PositiveSmallIntegerField()

    class Meta:
         ordering = ["slot"]
         constraints = [
            models.UniqueConstraint(
                fields=["build", "slot"],
                name="uniqe_build_item_slot"
            ),
            models.CheckConstraint(
                condition=models.Q(slot__gte=1, slot__lte=5),
                name="build_item_slot_range",
            ),
         ]



class BuildBoot(models.Model):
    build = models.ForeignKey(
         Build,
         on_delete=models.CASCADE,
         related_name="build_boots"
    )
    boot = models.ForeignKey(Item, on_delete=models.CASCADE)
    slot = models.PositiveSmallIntegerField()

    class Meta:
         ordering = ["slot"]
         constraints = [
              models.UniqueConstraint(
                   fields=["build", "slot"],
                   name="Unique_build_boot_slot"
              ),
              models.CheckConstraint(
                   condition=models.Q(slot__gte=1, slot__lte=2),
                   name="build_boot_slot_range",
              ),
         ]


     
class BuildRune(models.Model):
    build = models.ForeignKey(
        Build,
        on_delete=models.CASCADE,
        related_name="build_runes" 
    )
    rune = models.ForeignKey(Rune, on_delete=models.CASCADE)
    slot = models.PositiveSmallIntegerField()

    class Meta:
         ordering = ["slot"]
         constraints = [
              models.UniqueConstraint(
                   fields=["build", "slot"],
                   name="unique_build_rune_slot"
              ),
              models.CheckConstraint(
                   condition=models.Q(slot__gte=1, slot__lte=5),
                   name="build_rune_slot_range",
              ),
         ]



class BuildSpell(models.Model):
     build = models.ForeignKey(
        Build,
        on_delete=models.CASCADE,
        related_name="build_spells"
     )
     spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
     slot = models.PositiveSmallIntegerField()

     class Meta:
          ordering = ["slot"]
          constraints = [
               models.UniqueConstraint(
                    fields=["build", "slot"],
                    name="unique_build_spell_slot"
               ),
               models.CheckConstraint(
                    condition=models.Q(slot__gte=1, slot__lte=2),
                    name="build_spell_slot_range",
               ),
          ]

