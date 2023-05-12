# Generated by Django 4.2.1 on 2023-05-11 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0009_extend_requester_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="requester",
            options={
                "ordering": ("first_name", "last_name"),
                "verbose_name": "Requester",
                "verbose_name_plural": "Requesters",
            },
        ),
        migrations.AddField(
            model_name="requester",
            name="added_on",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Added on",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="requester",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Active"),
        ),
        migrations.AddField(
            model_name="requester",
            name="last_modified",
            field=models.DateTimeField(auto_now=True, verbose_name="Last Modified"),
        ),
    ]
