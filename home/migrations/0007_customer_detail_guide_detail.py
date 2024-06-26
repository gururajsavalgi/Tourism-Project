# Generated by Django 5.0.3 on 2024-04-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_detail',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='guide_detail',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
    ]
