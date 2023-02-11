# Generated by Django 4.1.5 on 2023-02-01 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_role'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='ads_pic/'),
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='title',
            field=models.CharField(default='test title', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ads.ad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
