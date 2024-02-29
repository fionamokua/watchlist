# Generated by Django 5.0.2 on 2024-02-29 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0002_remove_watchlist_platform"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist",
                to="watchlist_app.streamingplartform",
            ),
            preserve_default=False,
        ),
    ]
