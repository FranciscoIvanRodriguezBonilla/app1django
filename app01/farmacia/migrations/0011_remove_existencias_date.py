# Generated by Django 3.1.2 on 2020-11-10 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0010_auto_20201027_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='existencias',
            name='date',
        ),
    ]
