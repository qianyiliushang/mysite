# coding:utf-8
__author__ = 'chenpengpeng'
from django import forms
from .models import SignUp
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class SingUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not domain == "changingedu":
            raise forms.ValidationError("请使用合法的轻轻邮箱")
        if not extension == "com":
            raise forms.ValidationError("请使用合法的.com轻轻邮箱")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name


class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    full_name = forms.CharField()
    message = forms.CharField()
