# Generated by Django 2.1.4 on 2018-12-31 04:41

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank='True', upload_to=''),
        ),
    ]