# Generated by Django 4.1 on 2023-08-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile_pic.png', upload_to='profile_pics'),
        ),
    ]