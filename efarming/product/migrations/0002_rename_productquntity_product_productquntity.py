# Generated by Django 3.2 on 2022-02-18 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productQuntity',
            new_name='productquntity',
        ),
    ]
