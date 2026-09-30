from django.db import models



class Rune(models.Model):

    class Role(models.TextChoices):

        PRIMARY = "primary", "Primary"
        SECONDARY = "secondary", "Secondary"


    class SecondaryCategory(models.TextChoices):

        DOMINATION = "domination", "Domination"
        PRECISION = "presision", "Presision"
        RESOLVE = "resolve", "Resolve"
        SORCERY = "sorcery", "Sorcery"

    name = models.CharField(max_length=32, unique=True)
    img_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    role = models.CharField(max_length=16, choices=Role.choices)

    secondary_category = models.CharField(max_length=16, 
                                          choices=SecondaryCategory.choices, 
                                          blank=True,
                                          null=True)

    def __str__(self):
        return self.name



class Spell(models.Model):
    
    name = models.CharField(max_length=32, unique=True)
    cooldown = models.IntegerField()
    img_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name