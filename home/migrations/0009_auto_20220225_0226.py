# Generated by Django 3.2 on 2022-02-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_author_blog_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday_open', models.CharField(max_length=12)),
                ('weekday_close', models.CharField(max_length=12)),
                ('weekend_open', models.CharField(max_length=12)),
                ('weekend_close', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name_plural': 'Opening Times',
            },
        ),
        migrations.RemoveField(
            model_name='entry',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]