# Generated by Django 2.2.5 on 2019-11-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0018_auto_20191116_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport_info',
            name='playlist',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
