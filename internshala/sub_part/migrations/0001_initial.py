# Generated by Django 3.0.5 on 2021-05-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_new_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pizzaname', models.CharField(max_length=20)),
                ('Foodtype', models.CharField(max_length=4)),
                ('Foodsize', models.CharField(max_length=10)),
                ('Pizzaprice', models.CharField(max_length=10)),
            ],
        ),
    ]
