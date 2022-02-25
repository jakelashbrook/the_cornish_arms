# Generated by Django 3.2 on 2022-02-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='dish_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='dish_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
