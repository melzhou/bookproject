# Generated by Django 2.2.7 on 2020-04-22 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0008_auto_20200422_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writing',
            old_name='w_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='writing',
            old_name='w_updated',
            new_name='updated',
        ),
    ]
