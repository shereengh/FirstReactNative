# Generated by Django 2.2.4 on 2019-08-31 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='owner',
        ),
    ]