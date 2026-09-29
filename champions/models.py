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

    #اگر زمانی نامی ساختیم بطور خودکار حالت slug ان دخیره میشود.
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


