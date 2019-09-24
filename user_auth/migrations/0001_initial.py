# Generated by Django 2.2.5 on 2019-09-19 14:15

from django.db import migrations, models
import user_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('phone_num', models.BigIntegerField(null=True, validators=[user_auth.models.phone_number_validation])),
                ('location', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]