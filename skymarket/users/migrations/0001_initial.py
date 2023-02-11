# Generated by Django 4.1.5 on 2023-02-01 00:52

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
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('role', models.CharField(choices=[('USR', 'user'), ('ADM', 'admin')], default='USR', max_length=3)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='avatars/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
