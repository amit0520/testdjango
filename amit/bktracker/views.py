from django.shortcuts import render
from django.http import HttpResponse
from . models import BKrecords


class CURLValues:
    rqstType: int
    plantID: int
    lineID: int
    bkngTime: int
    T1: int
    T2: int
    T3: int
    T4: int
    T5: int
    T6: int

def idb(request):

    CURLValues.rqstType = int(request.GET['RQSTTYPE'])
    CURLValues.plantID = int(request.GET['PLANTID'])
    CURLValues.lineID = int(request.GET['LINEID'])
    CURLValues.bkngTime = int(request.GET['BAKETIME'])
    CURLValues.T1 = int(request.GET['T1'])
    CURLValues.T2 = int(request.GET['T2'])
    CURLValues.T3 = int(request.GET['T3'])
    CURLValues.T4 = int(request.GET['T4'])
    CURLValues.T5 = int(request.GET['T5'])
    CURLValues.T6 = int(request.GET['T6'])

    ret = BKrecords.objects.create(
        plantID=CURLValues.plantID,
        lineID=CURLValues.lineID,
        bkTime=CURLValues.bkngTime,
        t1=CURLValues.T1,
        t2=CURLValues.T2,
        t3=CURLValues.T3,
        t4=CURLValues.T4,
        t5=CURLValues.T5,
        t6=CURLValues.T6)
    # return HttpResponse("Got One Data***")
    return render(request, "records.html", {'bkValues':CURLValues})

#http://www.xyz.com/britanniaService/services.php?RQSTTYPE=1&PLANTID=1&LINEID=1
# &PRODID=1&BAKETIME=223&T1=366&T2=380&T3=355&T4=367&T5=366&T6=342

#http://127.0.0.1:8000/idb?RQSTTYPE=1&PLANTID=1&LINEID=1&PRODID=1&BAKETIME=223&T1=366&T2=380&T3=355&T4=367&T5=366&T6=342
#http://127.0.0.1:8000/idb?RQSTTYPE=1&PLANTID=1&LINEID=1&BAKETIME=223&T1=366&T2=380&T3=355&T4=367&T5=366&T6=342

def home(request):
    records = BKrecords.objects.all()
    return render(request, "index.html", {'records':records})