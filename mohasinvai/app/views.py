from django.http import request
from django.shortcuts import render
from .models import *
from datetime import date
# Create your views here.
def index(request):
    today=date.today()
    debit=Debit.objects.filter(Date=today)
    credit=Credit.objects.filter(Date=today)
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
    }
    return render(request,"index.html",sendvar)

def add(request):
    head=request.POST.get("headname")
    amount=request.POST.get("amount")
    deposit=request.POST.get("deposit")
    if request.method=="POST":
        if deposit=="Debit":
            fm=Debit(Head_Name=head,Amount=amount)
            fm.save()
            return render(request,"add.html",{"secces":"Deposit add successfully In Debit"})
        else:
            fm=Credit(Head_Name=head,Amount=amount)
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