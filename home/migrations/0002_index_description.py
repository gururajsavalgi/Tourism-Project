# Generated by Django 5.0.3 on 2024-04-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='description',
            field=models.TextField(default=''),
        ),
    ]