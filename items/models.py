from django.db import models
from django.utils.text import slugify



class ItemType(models.Model):

    class Code(models.TextChoices):

        BASIC = "basic", "Basic"
        MID_LEVEL = "mid_tier", "Mid tier"
        FIGHTER = "fighter", "Fighter"
        ASSASSIN = "assassin", "Assassin"
        MARKSMAN = "marksman", "Marksman"
        MAGIC = "magic", "Magic"
        DEFENSE = "defense", "Defense"
        SUPPORT = "support", "Support"
        BOOT1 = "basic_boot", "Basic boot"
        BOOT2 = "mid_tier_boot", "Mid_tier_boot"
        BOOT3 = "upgraded", "Upgraded"

    code = models.CharField(max_length=16, choices=Code.choices, blank=True)

    class Meta:
        db_table = "champions_itemtype"

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


    type = models.ManyToManyField(ItemType, related_name="items", db_table="champions_item_type")
     
    class Meta:
        db_table = "champions_item"

    def __str__(self):
        return f"{self.name}"


class ItemBuildPath(models.Model):

     item = models.ForeignKey( Item, on_delete=models.CASCADE, 
                              related_name="build_paths",)

     component = models.ForeignKey(Item, on_delete=models.CASCADE, 
                                   related_name="used_in_builds")

     order = models.PositiveIntegerField(default=0)

     class Meta:
        ordering = ["order"]
        db_table = "champions_itembuildpath"

     def __str__(self):
        return f"{self.component.name} --> {self.item.name}"