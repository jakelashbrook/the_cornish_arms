# Generated by Django 3.2 on 2022-02-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='number_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
