# Generated by Django 2.2.4 on 2019-08-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_auto_20190831_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
