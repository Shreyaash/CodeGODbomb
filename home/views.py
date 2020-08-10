
from django.http import HttpResponse
from django.shortcuts import render
from .models import Attackinfo
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


    # from subprocess import Popen, PIPE
    # #
    # # p = Popen(["python3", "manage.py","runscript","cf","--script-args",f"{mobile_no}",f"{frequency_no}"], cwd="/home/ubuntu/rdxbomb", stdout=PIPE, stderr=PIPE)
    # p = Popen(["python3", "cf.py"], cwd="/home/ubuntu/rdxbomb", stdout=PIPE, stderr=PIPE)

    os.system(f"nohup /home/ubuntu/env/bin/python3 rdxbomb.py {mobile_no} {frequency_no} &")

    # os.system(f"nohup /home/ubuntu/env/bin/python3 manage.py runscript cf --script-args {mobile_no} {frequency_no} &")

    datasend = {"texts" :f"ATTACK STARTED  WITH  : MOBILE NUMBER :{mobile_no}  AND WITH {frequency_no} SMS "}

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


    os.system(f"nohup /home/ubuntu/env/bin/python3 rdxcallbomber.py {mobile_no} {frequency_no} &")

    datasend = {"texts" :f"CALLATTACK COMPLETE WITH  : MOBILE NUMBER :{mobile_no}  AND WITH {frequency_no} CALLS"}
    print(datasend["texts"])

    return render(request,'attackresult.html',datasend)

