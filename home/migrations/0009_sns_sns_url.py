# Generated by Django 2.1.4 on 2018-12-31 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20181231_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='sns',
            name='sns_url',
            field=models.CharField(default='test', max_length=60, verbose_name='SNS Url'),
            preserve_default=False,
        ),
    ]
