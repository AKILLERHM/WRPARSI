from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("champions", "0021_move_items_to_items"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],

            state_operations=[
                migrations.CreateModel(
                    name="ItemType",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "code",
                            models.CharField(
                                blank=True,
                                choices=[
                                    ("basic", "Basic"),
                                    ("mid_tier", "Mid tier"),
                                    ("fighter", "Fighter"),
                                    ("assassin", "Assassin"),
                                    ("marksman", "Marksman"),
                                    ("magic", "Magic"),
                                    ("defense", "Defense"),
                                    ("support", "Support"),
                                    ("basic_boot", "Basic boot"),
                                    ("mid_tier_boot", "Mid_tier_boot"),
                                    ("upgraded", "Upgraded"),
                                ],
                                max_length=16,
                            ),
                        ),
                    ],
                    options={
                        "db_table": "champions_itemtype",
                    },
                ),

                migrations.CreateModel(
                    name="Item",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "name",
                            models.CharField(
                                max_length=64,
                                unique=True,
                            ),
                        ),
                        (
                            "slug",
                            models.SlugField(
                                blank=True,
                                null=True,
                            ),
                        ),
                        (
                            "price",
                            models.IntegerField(),
                        ),
                        (
                            "image_url",
                            models.URLField(
                                blank=True,
                            ),
                        ),
                        (
                            "description",
                            models.TextField(
                                blank=True,
                            ),
                        ),
                        (
                            "stats",
                            models.TextField(
                                blank=True,
                            ),
                        ),
                        (
                            "type",
                            models.ManyToManyField(
                                db_table="champions_item_type",
                                related_name="items",
                                to="items.itemtype",
                            ),
                        ),
                    ],
                    options={
                        "db_table": "champions_item",
                    },
                ),

                migrations.CreateModel(
                    name="ItemBuildPath",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "order",
                            models.PositiveIntegerField(
                                default=0,
                            ),
                        ),
                        (
                            "component",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="used_in_builds",
                                to="items.item",
                            ),
                        ),
                        (
                            "item",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="build_paths",
                                to="items.item",
                            ),
                        ),
                    ],
                    options={
                        "ordering": ["order"],
                        "db_table": "champions_itembuildpath",
                    },
                ),
            ],
        ),
    ]