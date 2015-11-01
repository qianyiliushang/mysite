__author__ = 'chenpengpeng'
# coding=utf-8
import sys
from django.shortcuts import render

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def about(request):
	return render(request, "about.html", {})




