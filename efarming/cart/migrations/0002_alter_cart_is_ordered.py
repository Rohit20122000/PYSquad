# Generated by Django 3.2 on 2022-02-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='is_ordered',
            field=models.BooleanField(default=False, max_length=50, verbose_name='Confirm'),
        ),
    ]
