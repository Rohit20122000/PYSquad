# Generated by Django 3.2 on 2022-02-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_cart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_quantity',
            field=models.TextField(),
        ),
    ]