# Generated by Django 5.0.3 on 2024-04-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_index_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='index',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]