# Generated by Django 2.2.3 on 2019-08-07 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchquery',
            options={'ordering': ['-pk']},
        ),
    ]
