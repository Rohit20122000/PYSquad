# Generated by Django 3.2 on 2022-02-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_auto_20220218_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorinventory',
            name='sell_price',
            field=models.IntegerField(default=2, help_text='price per Kg'),
            preserve_default=False,
        ),
    ]
