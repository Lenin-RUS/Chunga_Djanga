# Generated by Django 3.0.4 on 2020-04-10 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaspoints', '0008_auto_20200410_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='point_from_country',
        ),
    ]