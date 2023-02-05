# Generated by Django 3.2.16 on 2023-02-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_spravochnik'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, upload_to='images/avatars', verbose_name='аватарка профиля'),
        ),
    ]
