# Generated by Django 2.1.4 on 2018-12-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181231_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='logo',
            field=models.CharField(default='logo', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='one_row',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
