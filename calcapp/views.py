from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    if request.method=="POST":
        num1 = int(request.POST["txtnum1"])
        num2 = int(request.POST["txtnum2"])
        ope = request.POST.get("btnsubmit")
        num = 0
        if ope=="+":
            num = num1 + num2
        elif ope=="-":
            num = num1 - num2
        elif ope=="*":
            num = num1 * num2
        else:
            num = num1/num2
        return render(request,"calcapp/calc.html",{"key":"Result is "+str(num)})
    else:    
       return render(request,"calcapp/calc.html")
