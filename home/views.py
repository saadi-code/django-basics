from django.shortcuts import render, redirect
from datetime import datetime
from home import models
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"saad is great",
        "variable2":"zubair is great"
    }
    return render (request,'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return render (request,'about.html')
   # return HttpResponse("this is about page")

def services(request):
    return render (request,'services.html')
    # return HttpResponse("this is service page")

def contact(request):
    if request.method =="POST":
        name  =  request.POST.get("name")
        Email =  request.POST.get("Email")
        phone =  request.POST.get("phone")
        desc  =  request.POST.get("desc")
        ins = models.contact(Name=name, Email=Email, phone=phone, desc= desc, date = datetime.today())
        ins.save()
        messages.success(request, "your massage has been sent!")
        return redirect('home')
        
    return render (request,'contact.html')
    # return HttpResponse("this is contect page")

    #saadbro111&&&***