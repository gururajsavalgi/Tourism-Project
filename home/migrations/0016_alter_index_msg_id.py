# Generated by Django 5.0.3 on 2024-04-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_index_id_index_msg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='msg_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]