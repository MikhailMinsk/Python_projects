# Generated by Django 2.2.3 on 2019-08-08 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-pk'], 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
    ]
