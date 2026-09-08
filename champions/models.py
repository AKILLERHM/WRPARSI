from django.db import models



class ChampionRole(models.Model):

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=64)

    class Meta:
             verbose_name = "Role"
             verbose_name_plural = "Roles"

    def __str__(self):
             return self.name

class Champion(models.Model):

    name = models.CharField(max_length=128, unique=True)
    name_parsi = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    title_parsi = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True, null=True)


    roles = models.ManyToManyField(ChampionRole, related_name="champions")

    class Meta:
         ordering = ["name"]

    def __str__(self):
        return self.name
