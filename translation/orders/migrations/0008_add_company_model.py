# Generated by Django 4.0.6 on 2022-08-04 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_add_outsource_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Company Name. Please input using the Latin alphabet, in uppercase, without the type of legal entity (i.e. no "LLC" and the like.', max_length=30, verbose_name='Name')),
                ('code', models.CharField(help_text='INN for the Russian entities or any kind of Tax Code or ID for foreign entities. Required field.', max_length=50, unique=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.AlterField(
            model_name='document',
            name='company',
            field=models.ForeignKey(blank=True, help_text='Company that this document is related to', null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.company', verbose_name='Company'),
        ),
    ]
