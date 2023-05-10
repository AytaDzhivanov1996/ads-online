# Generated by Django 3.2.6 on 2023-05-03 13:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', max_length=10, verbose_name='роль')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]