# Generated by Django 5.0.3 on 2024-04-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_index_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
