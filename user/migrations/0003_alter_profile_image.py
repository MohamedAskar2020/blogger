# Generated by Django 4.1.3 on 2022-11-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/man-person-icon.png', upload_to='profile_pics'),
        ),
    ]
