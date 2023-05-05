# Generated by Django 4.2.1 on 2023-05-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0008_add_company_model"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="requester",
            name="orders_requester_unique_relationships",
        ),
        migrations.RemoveField(
            model_name="requester",
            name="name",
        ),
        migrations.AddField(
            model_name="requester",
            name="first_name",
            field=models.CharField(
                default="",
                help_text="First name of the requester.",
                max_length=50,
                verbose_name="First Name",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="requester",
            name="last_name",
            field=models.CharField(
                default="",
                help_text="Last name of the requester.",
                max_length=50,
                verbose_name="Last Name",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="requester",
            name="middle_name",
            field=models.CharField(
                blank=True,
                help_text="Middle Name of the requester.",
                max_length=50,
                verbose_name="Middle Name",
            ),
        ),
        migrations.AddConstraint(
            model_name="requester",
            constraint=models.UniqueConstraint(
                fields=("first_name", "middle_name", "last_name", "email"),
                name="orders_requester_unique_relationships",
            ),
        ),
    ]