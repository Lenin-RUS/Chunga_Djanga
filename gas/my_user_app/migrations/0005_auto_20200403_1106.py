# Generated by Django 3.0.4 on 2020-04-03 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_user_app', '0004_auto_20200320_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_user_app.Place_of_job'),
        ),
    ]
