from django.shortcuts import render
from app.models import *
# Create your views here.

from django.http import HttpResponse


def display_topic(request):
    ATO=Topic.objects.all()

    d={"ATO":ATO}

    return render(request,'display_topic.html',d)


def display_webpage(request):
    AWO=Webpage.objects.all()
    d={'AWO':AWO}
    return render(request,'display_webpage.html',d)


def display_access(request):
    AAO=AccessRecords.objects.all()
    d={'AAO':AAO}
    return render(request,'display_access.html',d)