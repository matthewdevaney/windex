# Generated by Django 2.1.3 on 2018-12-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockindex_app', '0007_auto_20181120_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observations',
            name='observation_date',
            field=models.DateTimeField(null=True),
        ),
    ]
