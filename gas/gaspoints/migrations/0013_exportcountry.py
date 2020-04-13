# Generated by Django 3.0.4 on 2020-04-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaspoints', '0012_delete_exportcountry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]