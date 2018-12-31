from django.contrib import admin
from .models import Setting, Bg_Image, About, Sns
# Register your models here.

class bg_ImageInline(admin.StackedInline):
    model = Bg_Image
    fields = ['position', 'photo']
    extra = 0

class SettingAdmin(admin.ModelAdmin):
    inlines = [bg_ImageInline]

    def save_model(self, request, obj, form, change):
        super(SettingAdmin, self).save_model(request, obj, form, change)

        for afile in request.FILES.getlist('photos_multiple'):
            obj.images.create(file=afile)

admin.site.register(Setting, SettingAdmin)
admin.site.register(About)
admin.site.register(Sns)