# Generated by Django 2.1.3 on 2018-12-27 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockindex_app', '0008_auto_20181210_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='high_price_52_weeks',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='low_price_52_weeks',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
