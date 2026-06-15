from django.shortcuts import render
from app.models import *

from django.db.models.functions import Length


from django.http import HttpResponse

from django.db.models import Q

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
    

    QSLWO=Webpage.objects.all()
    QSLWO=Webpage.objects.filter(topic_name='Cricket' , name="Bunty")

    QSLWO=Webpage.objects.all()
    QSLWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name="ronaldo"))




    LWO=Webpage.objects.all().values('name')
    print(LWO)

    LWO=Webpage.objects.all().values_list('name')
    print(LWO)

    LWO=Webpage.objects.all().only('name')
    print(LWO)
    

    LWO=Webpage.objects.all().defer('name')
    print(LWO)
    
    d={'QSLWO':QSLWO}
    return render(request,'display_webpage.html',d)


































def display_access(request):
    AAO=AccessRecords.objects.all()
    

    AAO=AccessRecords.objects.filter(date__year='2026')
    AAO=AccessRecords.objects.filter(date__month__gte='6')
    AAO=AccessRecords.objects.filter(date__day__lte='20')





    d={'AAO':AAO}
    return render(request,'display_access.html',d)