# Generated by Django 3.0.5 on 2021-05-10 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0004_remove_menuorder_pizzaorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuorder',
            name='Toppings',
        ),
    ]