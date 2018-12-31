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
    setting = models.ForeignKey(Setting, related_name="images", on_delete=models.CASCADE)
    photo = ProcessedImageField(
        format='JPEG',
        options={'quality': 90},
    )
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s' % (self.setting, self.photo)

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
        ('ti-facebook', '페이스북'),
        ('ti-github', '깃허브'),
        ('ti-youtube', '유튜브'),
        ('ti-instagram', '인스타그램'),
        ('ti-twitter-alt', '트위터')
    )
    sns_type = models.CharField('SNS 종류', choices=sns_type_status, max_length=30)
    sns_url = models.CharField('SNS Url', max_length=60)

    def __str__(self):
        return self.sns_url