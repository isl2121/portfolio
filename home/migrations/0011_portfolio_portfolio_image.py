# Generated by Django 2.1.4 on 2019-01-02 01:38

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190101_0319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('image', '이미지형식'), ('youtube', '유튜브영상')], max_length=20, verbose_name='포트폴리오 타입')),
                ('main_img', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('main_title', models.CharField(max_length=30, verbose_name='메인글')),
                ('used_info', models.CharField(choices=[('y', '사용'), ('n', '사용안함')], default='n', max_length=5, verbose_name='추가설명')),
                ('content', models.TextField(verbose_name='설명글')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.Portfolio')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]