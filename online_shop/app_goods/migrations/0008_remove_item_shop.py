# Generated by Django 3.2.16 on 2023-02-04 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0007_auto_20230129_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='shop',
        ),
    ]
