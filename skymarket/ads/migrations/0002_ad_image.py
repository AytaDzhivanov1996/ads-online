# Generated by Django 3.2.6 on 2023-05-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads/', verbose_name='Изображение'),
        ),
    ]
