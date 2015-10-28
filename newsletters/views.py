# coding=utf-8
import sys
from django.shortcuts import render

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def home(request):
    title = "欢迎"
    # if request.user.is_authenticated():
    #    title = "标题 %s" % (request.user)
    context = {
        "title": title,
    }
    return render(request, "home.html", context)
