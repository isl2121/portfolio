from django.shortcuts import render
from .models import Setting, Bg_Image, About, Sns
from django.core.mail import EmailMessage
from .forms import mailform
# Create your views here.

def main(request):

    data = Setting.objects.first()
    form = mailform()

    if request.method == 'POST':
        form = mailform(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            receiver = data.user_mail
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print(form.cleaned_data, receiver)
            message = message + "    메일 :" + mail + "     이름 : " + name
        try:
            email = EmailMessage(subject, message, to=[receiver])
            result = email.send()
            print(email,result)
        except Exception as e:

            print(e)


    try:
        bg_image = Bg_Image.objects.filter(setting=data.id)
    except:
        bg_image = None

    if data.using_sns:
        try:
            sns_list = Sns.objects.all()
        except:
            sns_list = None

    abouts = About.objects.all()


    return render(request, 'home/main.html', {'data':data, 'bg_img':bg_image,'abouts':abouts, 'sns_list': sns_list, 'form': form} )