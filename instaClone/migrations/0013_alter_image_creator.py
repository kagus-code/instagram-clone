# Generated by Django 3.2.3 on 2021-05-23 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaClone', '0012_alter_image_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='instaClone.profile'),
        ),
    ]