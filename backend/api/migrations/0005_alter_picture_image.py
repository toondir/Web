# Generated by Django 5.1.3 on 2024-12-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='picture/'),
        ),
    ]
