# Generated by Django 5.0.3 on 2024-04-27 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_index_rating_index_review_index_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='index',
            name='review',
        ),
    ]
