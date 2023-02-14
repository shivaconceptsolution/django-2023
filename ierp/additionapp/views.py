from django.shortcuts import render
from django.http import HttpResponse
def add(request):
    a,b=10,2
    return HttpResponse("Result is "+str(a+b))
def sub(request):
     a,b=10,2
     return HttpResponse("Result is "+str(a-b))   
