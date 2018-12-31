from django.shortcuts import render
from .models import Setting, Bg_Image, About
# Create your views here.

def main(request):
    data = Setting.objects.first()
    try:
        bg_image = Bg_Image.objects.filter(setting=data.id)
    except:
        bg_image = None

    abouts = About.objects.all()


    return render(request, 'home/main.html', {'data':data, 'bg_img':bg_image,'abouts':abouts} )