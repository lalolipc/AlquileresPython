# Generated by Django 2.2.12 on 2020-10-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airbnb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='No name provided', max_length=50),
        ),
    ]