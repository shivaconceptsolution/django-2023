from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method=="POST":
        a = request.POST["txtnum1"]
        b = request.POST["txtnum2"]
        c = int(a)+ int(b)
        return HttpResponse("Result is "+str(c))
    return render(request,"designapp/welcome.html")
