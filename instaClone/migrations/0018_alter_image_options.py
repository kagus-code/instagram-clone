# Generated by Django 3.2.3 on 2021-05-24 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaClone', '0017_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-pub_date']},
        ),
    ]
