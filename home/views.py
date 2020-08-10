
from django.http import HttpResponse
from django.shortcuts import render
from .models import Attackinfo
from .models import Userinfo
from .models import Workerinfo
import multiprocessing
import time


def index(request):
    # params = {"name":"raman dahiya","place":"shamli"}
    return  render(request,'index.html')

def callbombindex(request):
    # params = {"name":"raman dahiya","place":"shamli"}
    return  render(request,'callbombindex.html')

def doattack(request):
    import os

    mobile_no = request.GET.get("mn")
    frequency_no = request.GET.get("fq")

    if mobile_no == "" or int(frequency_no) < 0 or len(mobile_no) != 10 or frequency_no == "" or (frequency_no.isdigit() == False) or (mobile_no.isdigit() == False) :
        datasend = {"texts": f"You Enter Invalid Details"}
        return render(request,'attackresult.html',datasend)


    Producti = Attackinfo( mobile_n = mobile_no, frequency_n=frequency_no)
    Producti.save()


    if int(frequency_no) >= 1000 :
        frequency_no = "1000"

    # os.system(f"nohup python3 rdxbomb.py {mobile_no} {frequency_no} &")
    # os.system(f"nohup python3 cf.py {mobile_no} {frequency_no} &")

    # from subprocess import Popen, PIPE
    # #
    # # p = Popen(["python3", "manage.py","runscript","cf","--script-args",f"{mobile_no}",f"{frequency_no}"], cwd="/home/ubuntu/rdxbomb", stdout=PIPE, stderr=PIPE)
    # p = Popen(["python3", "cf.py"], cwd="/home/ubuntu/rdxbomb", stdout=PIPE, stderr=PIPE)

    # os.system(f"sudo python3 rdxbomb.py {mobile_no} {frequency_no}")
    # os.system(f"sudo bash com.sh")
    os.system(f"nohup /home/ubuntu/env/bin/python3 rdxbomb.py {mobile_no} {frequency_no} &")
    # os.system(f"nohup /home/ubuntu/env/bin/python3 manage.py runscript cf --script-args {mobile_no} {frequency_no} &")
    # os.system(f"nohup python3 manage.py runscript cf --script-args 8171247161 5 &")
    # os.system(f"nohup python3 rdxbomb.py {mobile_no} {frequency_no} &")

    datasend = {"texts" :f"ATTACK STARTED 4 WITH  : MOBILE NUMBER :{mobile_no}  AND WITH {frequency_no} SMS  {os.getcwd()}"}
    # datasend = {"texts" :f"ATTACK STARTED fc WITH  : MOBILE NUMBER :{mobile_no}  AND WITH {frequency_no} SMS "}

    print(datasend["texts"])

    return render(request,'attackresult.html',datasend)



def docallattack(request):
    import os
    import time
    import datetime
    import random

    mobile_no = request.GET.get("mn")
    frequency_no = request.GET.get("fq")

    if mobile_no == "" or int(frequency_no) < 0 or len(mobile_no) != 10 or frequency_no == "" or (frequency_no.isdigit() == False) or (mobile_no.isdigit() == False) :
        datasend = {"texts": f"You Enter Invalid Details"}
        return render(request,'attackresult.html',datasend)


    Producti = Attackinfo( mobile_n = mobile_no, frequency_n=frequency_no)
    Producti.save()


    if int(frequency_no) >= 10 :
        frequency_no = "10"



    # ------------------------ UPDATE DATABASE ---------------------

    def updatedatabase():
        workers_list = ["worker0", "worker1", "worker2", "worker3"]
        for i in workers_list:
            swor = Workerinfo.objects.get(workername=i)
            swor_ctime = swor.workerctime
            swor_rtime = swor.workerrtime

            swor_dto = datetime.datetime.strptime(swor_ctime, '%Y-%m-%d %H:%M:%S.%f')

            ctime = datetime.datetime.now()
            delta = ctime - swor_dto
            worrsec = delta.total_seconds()

            print(f"working sec {worrsec}")
            print(f"sworr itme sec {swor_rtime}")

            if int(worrsec) > int(swor_rtime):
                swor.status = "free"
                swor.save()

    # -----------------------------------------------------------------

    updatedatabase()


    worker0 = f"heroku run:detached python rdxcallbomber.py {mobile_no} {frequency_no}  --app rdxbomber"
    worker1= f"heroku run:detached python rdxcallbomber.py {mobile_no} {frequency_no}  --app rdxbomber1"
    worker2 = f"heroku run:detached python rdxcallbomber.py {mobile_no} {frequency_no}  --app rdxbomber2"
    worker3 = f"heroku run:detached python rdxcallbomber.py {mobile_no} {frequency_no}  --app rdxbomber3"


    awor = Workerinfo.objects.filter(status="free")

    for_wrkr1 = Workerinfo.objects.get(workername="worker1")
    ctime = for_wrkr1.workerctime
    rtime = for_wrkr1.workerrtime
    time_c_worker = datetime.datetime.strptime(ctime, '%Y-%m-%d %H:%M:%S.%f')


    curr_time = datetime.datetime.now()

    time_left_in_Sec = time_c_worker - curr_time

    totalsecleft = time_left_in_Sec.total_seconds()
    totalsecleft += int(rtime)


    if len(awor) == 0:
        datasend = {"texts": f"ALL SERVERS ARE BUSY TILL NOW PLEASE TRY SOME TIME LATER TRY AGAIN AFTER IN {round(int(totalsecleft)/60,2)} MINUTE"}
        return render(request, 'attackresult.html', datasend)

    wrknn = awor[0].workername
    wrkn = Workerinfo.objects.get(workername=wrknn)
    wrkn.workerctime = datetime.datetime.now()
    wrkn.workerrtime = str(int(frequency_no) * 12)
    wrkn.status = "working"
    wrkn.save()

    numberofworker = wrknn[6:7]

    if int(numberofworker) == 0:
        numberofworker = ""

    os.system(f"heroku run:detached python rdxcallbomber.py {mobile_no} {frequency_no}  --app rdxbomber{numberofworker}")

    datasend = {"texts" :f"ATTACK COMPLETE WITH  : MOBILE NUMBER :{mobile_no}  AND WITH {frequency_no} CALLS WITH SERVER  : RDXBOMBSERVER{numberofworker}"}
    print(datasend["texts"])

    return render(request,'attackresult.html',datasend)

