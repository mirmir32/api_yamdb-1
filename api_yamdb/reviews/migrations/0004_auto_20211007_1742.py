# Generated by Django 2.2.16 on 2021-10-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20211006_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.IntegerField(),
        ),
    ]
