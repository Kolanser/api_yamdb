# Generated by Django 2.2.16 on 2022-08-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220828_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id']},
        ),
    ]
