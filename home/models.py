from django.db import models
from django.template.defaultfilters import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.core.exceptions import ValidationError

# Create your models here.
class Setting (models.Model):
    Skins_status = (
        ('default.css', 'default'),
        ('amber.css', 'amber'),
        ('blue.css', 'blue'),
        ('blue-grey.css', 'blue-grey'),
        ('brown.css', 'brown'),
        ('cyan.css', 'cyan'),
        ('deep-orange.css', 'deep-orange'),
        ('deep-purple.css', 'deep-purple'),
        ('green.css', 'green'),
        ('indigo.css', 'indigo'),
        ('light-blue.css', 'light-blue'),
        ('light-green.css', 'light-green'),
        ('lime.css', 'lime'),
        ('orange.css', 'orange'),
        ('pink.css', 'pink'),
        ('purple.css', 'purple'),
        ('red.css', 'red'),
        ('teal.css', 'teal'),
        ('yellow.css', 'yellow'),
    )


    title = models.CharField('타이틀', max_length=30)
    logo = models.CharField('메인화면로고',max_length=30)
    one_row = models.CharField('1줄',max_length=80)
    user_mail = models.CharField('이메일', max_length=60)
    skin_type = models.CharField('스킨', max_length=20, choices=Skins_status, default='default.css')
    using_sns = models.BooleanField('SNS 사용여부', default=True )

    def get_image_filename(instance, filename):
        title = instance.setting.title
        slug = slugify(title)
        return "setting_images/%s-%s" % (slug, filename)

    def clean(self):
        if Setting.objects.exclude(id=self.id).count():
            raise ValidationError('설정은 하나만 가능합니다.')

    def __str__(self):
        return self.title

class Bg_Image(models.Model):
    setting = models.ForeignKey(Setting, related_name="bg_images", on_delete=models.CASCADE)
    photo = ProcessedImageField(
        format='JPEG',
        options={'quality': 90},
    )
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s' % (self.setting, self.photo)

class Portfolio (models.Model):
    portfolio_type = (
        ('image', '이미지형식'),
    )

    info_type = (
        ('y', '사용'),
        ('n', '사용안함')
    )
    type = models.CharField('포트폴리오 타입', choices=portfolio_type, max_length=20)
    main_img = ProcessedImageField(
        processors=[Thumbnail(346, 346)],
        format='JPEG',
        options={'quality': 90},
    )
    main_title = models.CharField('제목', max_length=30)
    sub_title = models.CharField('부제목', max_length=30, blank=True, null=True)
    content = models.TextField('설명글')
    used_info = models.CharField('추가설명', max_length=5, default='n', choices=info_type)

    info_title1 = models.CharField('INFO 타이틀1', max_length=30, blank=True, null=True)
    info_content1 = models.TextField('INFO 내용1', blank=True, null=True)
    info_title2 = models.CharField('INFO 타이틀2', max_length=30, blank=True, null=True)
    info_content2 = models.TextField('INFO 내용2', blank=True, null=True)
    info_title3 = models.CharField('INFO 타이틀3', max_length=30, blank=True, null=True)
    info_content3 = models.TextField('INFO 내용3', blank=True, null=True)
    info_url = models.CharField('INFO url', max_length=30, blank=True, null=True)


    def __str__(self):
        return self.main_title


class Portfolio_Image(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name="portfolio_images", on_delete=models.CASCADE)
    photo = ProcessedImageField(
        format='JPEG',
        options={'quality': 90},
    )
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s' % (self.portfolio, self.photo)


class About (models.Model):
    title = models.TextField(null=True, blank=True)
    photo = ProcessedImageField(
        format='JPEG',
        options={'quality': 90},
        blank='True',
    )
    content = models.TextField()

    def __str__(self):
        return self.content


class Sns (models.Model):
    sns_type_status = (
        ('ti-facebook', 'FaceBook'),
        ('ti-github', 'Github'),
        ('ti-youtube', 'Youtube'),
        ('ti-instagram', 'Instagram'),
        ('ti-twitter-alt', 'Twitter')
    )
    sns_type = models.CharField('SNS 종류', choices=sns_type_status, max_length=30)
    sns_url = models.CharField('SNS Url', max_length=60)

    def __str__(self):
        return self.get_sns_type_display()