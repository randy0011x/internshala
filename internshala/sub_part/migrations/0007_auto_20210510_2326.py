# Generated by Django 3.0.5 on 2021-05-10 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_auto_20210510_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuorder',
            name='Foodsize',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuorder',
            name='Foodtype',
            field=models.CharField(default=django.utils.timezone.now, max_length=4),
            preserve_default=False,
        ),
    ]
