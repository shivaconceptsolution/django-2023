from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello World")
def marksheet(request):
    marks = {"PHY":45,"Chem":29,"Math":87,"Eng":98,"Hindi":56}
    c=0
    total=0
    dist=""
    result=""
    gm=0
    s=""
    for k,v in marks.items():
        total+=v
        if v>=75:
            dist += k + " "
        if v<33:
            s+=k+ " "
            gm=v
            c=c+1
    else:
        if c==0 or (c==1 and gm>=28):
            if c==0:
              per = total/5
              result = "Pass "
            else:
             per= (total+(33-gm))/5
             result = "pass with grace in "+s  
            if per>=33 and per<45:
                result += " by third division"
            elif per<60:
                result += " by second division"  
            else:
                result += " by first division"  
            if dist!=" ":
                result += ", distinction subject is "+ dist 
        elif c==1:
            result = "suppl in "+s 
        else:
            result= "fail in "+s
    return HttpResponse(result)               



