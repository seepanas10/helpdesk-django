# Generated by Django 4.0.6 on 2022-07-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticknum',
            field=models.IntegerField(null=True),
        ),
    ]
