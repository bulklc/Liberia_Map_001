# Generated by Django 2.2.5 on 2019-09-08 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=17),
        ),
        migrations.AlterField(
            model_name='shop',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=17),
        ),
    ]
