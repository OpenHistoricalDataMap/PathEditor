# Generated by Django 2.1.5 on 2019-01-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom_id', models.IntegerField(default=0)),
                ('geom', models.CharField(max_length=1000)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
