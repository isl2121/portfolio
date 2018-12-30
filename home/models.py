from django.db import models
from django.template.defaultfilters import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Setting (models.Model):
    title = models.CharField(max_length=30)

    def get_image_filename(instance, filename):
        title = instance.setting.title
        slug = slugify(title)
        return "setting_images/%s-%s" % (slug, filename)


class Image(models.Model):
    setting = models.ForeignKey(Setting, related_name="images")
    file =  photo = ProcessedImageField(
        format='JPEG',
        options={'quality': 90},
        blank='True',
    )
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

        def __str__(self):
            return self.file