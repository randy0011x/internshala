# Generated by Django 3.0.5 on 2021-05-10 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_menuorder_toppings'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuorder',
            name='Pizzaorder',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
