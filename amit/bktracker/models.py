from django.db import models

#http://www.xyz.com/britanniaService/services.php?RQSTTYPE=1&PLANTID=1&LINEID=1&PRODID=1&BAKETIME=223&T1=366&T2=380&T3=355&T4=367&T5=366&T6=342


class BKrecords(models.Model):
    t1 = models.IntegerField()
    t2 = models.IntegerField()
    t3 = models.IntegerField()
    t4 = models.IntegerField()
    t5 = models.IntegerField()
    t6 = models.IntegerField()
    plantID = models.CharField(max_length=10)
    lineID = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)
    bkTime = models.IntegerField()

    class Meta:
        db_table = "bk_records"