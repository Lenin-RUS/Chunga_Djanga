# Generated by Django 3.0.3 on 2020-02-16 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaspoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointKey', models.CharField(max_length=32, unique=True)),
                ('pointLabel', models.TextField()),
                ('point_id', models.CharField(max_length=32, unique=True)),
                ('commercialType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaspoints.CommercialType')),
                ('pointType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaspoints.PointType')),
            ],
        ),
        migrations.RemoveField(
            model_name='points',
            name='commercialType',
        ),
        migrations.RemoveField(
            model_name='points',
            name='infrastructureLabel',
        ),
        migrations.RemoveField(
            model_name='points',
            name='pointType',
        ),
        migrations.DeleteModel(
            name='InfrastructureLabel',
        ),
        migrations.DeleteModel(
            name='Points',
        ),
    ]