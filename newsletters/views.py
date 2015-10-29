# coding=utf-8
import sys
from django.shortcuts import render
from .forms import SingUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def home(request):
    title = "欢迎"
    form = SingUpForm(request.POST or None)
    # if request.method == 'POST':
    #   print(request.POST)
    # if request.user.is_authenticated():
    #    title = "标题 %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            instance.full_name = "zombie"
        instance.save()
        # print instance.email
        # print instance.timestamp
        context = {
             "title": "welcome back"
         }
    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key in form.cleaned_data.iteritems():
            print(key, form.cleaned_data.get(key))

        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        message = form.cleaned_data.get("message")
        send_mail('Email for test', message, email, [email],
                  fail_silently=False)

    context = {
        "form": form,
    }

    return render(request, "contact.html", context)
