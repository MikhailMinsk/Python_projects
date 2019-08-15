# Generated by Django 2.2.4 on 2019-08-15 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_additionalimage_ads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('content', models.TextField(verbose_name='Content')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Show comment?')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')),
                ('ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Ads', verbose_name='Ad')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['created'],
            },
        ),
    ]
