# Generated by Django 3.0.4 on 2020-05-09 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200508_2243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['name']},
        ),
    ]
