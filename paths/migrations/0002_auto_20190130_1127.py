# Generated by Django 2.1.5 on 2019-01-30 11:27

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypath',
            name='spots',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='geo_object.GeoObject'),
        ),
    ]
