from django.shortcuts import render

def home(request):
    return render(request,"fivepages/home.html")
def aboutus(request):
    return render(request,"fivepages/about.html")
def services(request):
    return render(request,"fivepages/services.html")
def gallery(request):
    return render(request,"fivepages/gallery.html")
def contactus(request):
    return render(request,"fivepages/contact.html")