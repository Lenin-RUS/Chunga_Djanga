# Generated by Django 3.0.4 on 2020-04-10 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaspoints', '0006_auto_20200410_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='point_from_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gaspoints.FromCountry'),
        ),
    ]
