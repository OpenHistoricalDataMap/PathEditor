# Generated by Django 2.1.5 on 2019-01-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo_object', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(default='Info about Path', max_length=200)),
                ('name', models.CharField(default='New Path', max_length=50)),
                ('valid_from', models.DateTimeField(null=True)),
                ('valid_until', models.DateTimeField(null=True)),
                ('source', models.URLField(null=True)),
                ('spots', models.ManyToManyField(to='geo_object.GeoObject')),
            ],
        ),
    ]
