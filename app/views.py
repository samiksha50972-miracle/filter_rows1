from django.shortcuts import render
from app.models import *

from django.db.models.functions import Length


from django.http import HttpResponse


def display_topic(request):
    ATO=Topic.objects.all()

    d={"ATO":ATO}

    return render(request,'display_topic.html',d)


def display_webpage(request):
    AWO=Webpage.objects.all()
    QSLWO=Webpage.objects.filter(topic_name='Kabaddi')
    QSLWO=Webpage.objects.exclude(topic_name='Kabaddi')
    QSLWO=Webpage.objects.all()[3:8:]   #slicing
    QSLWO=Webpage.objects.all().order_by('name') 
    QSLWO=Webpage.objects.all().order_by('-name')




    QSLWO=Webpage.objects.all().order_by(Length('name'))
    QSLWO=Webpage.objects.all().order_by(Length('name').desc())




    QSLWO=Webpage.objects.filter(pk__in=(2,5,6,7))   #column_name__fieldsLookUps
    QSLWO=Webpage.objects.exclude(pk__in=[2,5,6,7])   #not in

    QSLWO=Webpage.objects.filter(pk__isnull=True)
    QSLWO=Webpage.objects.filter(pk__isnull=False)

    QSLWO=Webpage.objects.filter(name__startswith='m')    #case in-sensitive
    QSLWO=Webpage.objects.filter(name__endswith='m')    #case in-sensitive
    QSLWO=Webpage.objects.filter(name__contains='a')    #case in-sensitive

    QSLWO=Webpage.objects.filter(pk__gt=4)    #case in-sensitive
    QSLWO=Webpage.objects.filter(pk__gte=5)    #case in-sensitive
    QSLWO=Webpage.objects.filter(pk__lt=4)    #case in-sensitive
    QSLWO=Webpage.objects.filter(pk__lte=4)    #case in-sensitive


    #for case sensitive use regex
    QSLWO=Webpage.objects.filter(name__regex='^m')    #case sensitive



    
    d={'QSLWO':QSLWO}
    return render(request,'display_webpage.html',d)


































def display_access(request):
    AAO=AccessRecords.objects.all()
    
    d={'AAO':AAO}
    return render(request,'display_access.html',d)