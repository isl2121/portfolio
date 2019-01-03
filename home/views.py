from django.shortcuts import render, get_object_or_404
from .models import Setting, Bg_Image, About, Sns, Portfolio, Portfolio_Image
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from .forms import mailform
from django.contrib import messages

# Create your views here.


def portfolio(request, pk):

    data = Portfolio.objects.prefetch_related('portfolio_images').get(pk=pk)

    return render(request, 'home/ajax/portfolio_info.html', {
        'data': data
    })

def main(request):

    data = Setting.objects.prefetch_related('bg_images').first()

    form = mailform()

    if request.method == 'POST':
        form = mailform(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            receiver = data.user_mail
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            message = message + "    메일 :" + mail + "     이름 : " + name
        try:
            email = EmailMessage(subject, message, to=[receiver])
            result = email.send()
            messages.info(request, '메일이 정상적으로 보내졌습니다.')
        except Exception as e:
            messages.error(request, '메일전송중 문제가 발생했습니다.')

        return HttpResponseRedirect('')


    if data.using_sns:
        try:
            sns_list = Sns.objects.all()
        except:
            sns_list = None

    try:
        pf_list = Portfolio.objects.all()
    except:
        pf_list = None

    abouts = About.objects.all()

    return_data = {
        'data': data,
        'abouts': abouts,
        'sns_list': sns_list,
        'form': form,
        'pf_list' : pf_list
    }


    return render(request, 'home/main.html',  return_data)