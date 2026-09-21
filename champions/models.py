from django.db import models
from django.utils.text import slugify


class ChampionRole(models.Model):

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


    roles = models.ManyToManyField(ChampionRole, related_name="champions")

    class Meta:
         ordering = ["name"]

    def __str__(self):
        return self.name


class Ability(models.Model):

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


class ItemType(models.Model):

    class Code(models.TextChoices):

        BASIC = "basic", "Basic"
        MID_LEVEL = "mid_level", "Mid level"
        PHYSICLA = "physical", "Physical"
        MAGICAL = "magical", "Magical"
        DEFENSIVE = "defensive", "Defensive"
        SUPPORT = "support", "Support"
        BOOT1 = "tier_1", "Tier 1"
        BOOT2 = "tier_2", "Tier 2"
        BOOT3 = "tier_3", "Tier 3"

    code = models.CharField(max_length=16, choices=Code.choices, blank=True)

    def __str__(self):
        return self.get_code_display()


class Item(models.Model):

    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
     
    price = models.IntegerField()
    image_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    stats = models.TextField(blank=True)


    type = models.ManyToManyField(ItemType, related_name="items")
     


    def __str__(self):
        return self.name
