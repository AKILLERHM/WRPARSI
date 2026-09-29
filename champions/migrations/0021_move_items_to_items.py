from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("champions", "0020_itembuildpath"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel(
                    name="ItemBuildPath",
                ),
                migrations.DeleteModel(
                    name="Item",
                ),
                migrations.DeleteModel(
                    name="ItemType",
                ),
            ],
        ),
    ]