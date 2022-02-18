# Generated by Django 3.2 on 2022-02-18 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_remove_vendorinventory_deniedbutton'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorinventory',
            old_name='Catagory',
            new_name='catagory',
        ),
        migrations.RenameField(
            model_name='vendorinventory',
            old_name='Dateforready',
            new_name='dateforready',
        ),
        migrations.RenameField(
            model_name='vendorinventory',
            old_name='acceptbutton',
            new_name='is_accept',
        ),
        migrations.RenameField(
            model_name='vendorinventory',
            old_name='ProductQuantity',
            new_name='productquantity',
        ),
        migrations.RenameField(
            model_name='vendorinventory',
            old_name='SubCatagory',
            new_name='subcatagory',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='areaname',
        ),
    ]
