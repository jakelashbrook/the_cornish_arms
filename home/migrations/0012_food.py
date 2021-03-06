# Generated by Django 3.2 on 2022-02-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220225_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.CharField(default='timezone.now', max_length=12)),
                ('tuesday', models.CharField(default='timezone.now', max_length=12)),
                ('wednesday', models.CharField(default='timezone.now', max_length=12)),
                ('thursday', models.CharField(default='timezone.now', max_length=12)),
                ('friday', models.CharField(default='timezone.now', max_length=12)),
                ('saturday', models.CharField(default='timezone.now', max_length=12)),
                ('sunday', models.CharField(default='timezone.now', max_length=12)),
                ('if_lunch', models.BooleanField(default=False)),
                ('lunch_hours', models.CharField(default='timezone.now', max_length=12)),
            ],
        ),
    ]
