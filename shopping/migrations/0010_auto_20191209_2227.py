# Generated by Django 2.2.5 on 2019-12-09 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_auto_20191209_2207'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='deliveryoptions',
            unique_together={('name_id', 'product', 'pincode')},
        ),
    ]