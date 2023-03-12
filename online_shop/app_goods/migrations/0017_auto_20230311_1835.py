# Generated by Django 3.2.16 on 2023-03-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0016_auto_20230311_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='account_number',
            field=models.IntegerField(default=1, verbose_name='номер счёта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='is_success',
            field=models.BooleanField(default=True),
        ),
    ]
