from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    if request.method=="POST":
        a = int(request.POST["txtnum1"])
        b = int(request.POST["txtnum2"])
        a,b=b,a
        return HttpResponse("After Swapping value of a="+str(a) + "b ="+str(b))

    return render(request,"swapapp/swap.html")

def si(request):
    if request.method=="POST":
        p = float(request.POST["txtp"])
        r = float(request.POST["txtr"])
        t = float(request.POST["txtt"])
        s = (p*r*t)/100
        return render(request,"swapapp/si.html",{"res":s,"p":p,"r":r,"t":t})

    return render(request,"swapapp/si.html")