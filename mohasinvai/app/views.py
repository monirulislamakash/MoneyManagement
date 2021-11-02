from django.http import request
from django.shortcuts import render
from .models import *
from datetime import date
# Create your views here.
from datetime import date,timedelta
def index(request):
    today=date.today()
    Odate=date.today()+timedelta(days=1)
    closing=request.POST.get("closing")
    if request.method=="POST":
        clo=Closing(Closing=closing)
        opa=Opaning(Date=Odate,Opaning=closing)
        clo.save()
        opa.save()
        return render(request,"index.html",{"close":"Close Today"})
    debit=Debit.objects.filter(Date=today)
    credit=Credit.objects.filter(Date=today)
    opana=Opaning.objects.filter(Date=today)
    debittem=0
    credittem=0
    for i in debit:
        ftemp=int(i.Amount)
        debittem=debittem+ftemp
    for i in credit:
        ftemp=int(i.Amount)
        credittem=credittem+ftemp
    total=credittem-debittem
    sendvar={
        'debit':debit,
        'credit':credit,
        "total_dabit":debittem,
        'total_credit':credittem,
        'total':total,
        "opaning":opana,
    }
    return render(request,"index.html",sendvar)
def monthly(request):
    deposit=request.POST.get("Deposit")
    datef=request.POST.get("datef")
    datet=request.POST.get("datet")
    if request.method=='POST':
        if deposit=="Debit":
            fm=Debit.objects.filter(Date__lte=datef,Date__gte=datet)
            sent={
                "debit":fm
            }
            return render(request,"monthly.html",sent)
        else:
            fm=Credit.objects.filter(Date__lte=datef,Date__gte=datet)
            sent={
                "credit":fm
            }
            return render(request,"monthly.html",sent)
    return render(request,"monthly.html")
def search(request):
    expens=request.POST.get("Expens")
    vawcher=request.POST.get("vawcher")
    if request.method=="POST":
        if expens!="Select Expens":
            fl=Debit.objects.filter(Expans_type=expens)
            fm=Credit.objects.filter(Expans_type=expens)
            sent={
                "credit":fm,
                "debit":fl
                    }
            return render(request,"monthly.html",sent)
        if vawcher!="":
            fl=Debit.objects.filter(Vaucher=vawcher)
            fm=Credit.objects.filter(Vaucher=vawcher)
            sent={
                "credit":fm,
                "debit":fl
                    }
            return render(request,"monthly.html",sent)
    return render(request,"monthly.html")
def add(request):
    head=request.POST.get("headname")
    amount=request.POST.get("amount")
    deposit=request.POST.get("deposit")
    expans=request.POST.get("expans")
    vaucher=request.POST.get("expans")
    if request.method=="POST":
        if deposit=="Debit":
            fm=Debit(Head_Name=head,Amount=amount,Expans_type=expans,Vaucher=vaucher)
            fm.save()
            return render(request,"add.html",{"secces":"Deposit add successfully In Debit"})
        else:
            fm=Credit(Head_Name=head,Amount=amount,Expans_type=expans,Vaucher=vaucher)
            fm.save()
            return render(request,"add.html",{"secces":"Deposit add successfully In Credit"})
    return render(request,"add.html")
def debit(request):
    debit=Debit.objects.all()
    sendvar={
       'debit':debit 
    }
    return render(request,"debit.html",sendvar)    
def credit(request):
    credit=Credit.objects.all()
    sendvar={
       'credit':credit 
    }
    return render(request,"credit.html",sendvar)