from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    userdata=UserDetail.objects.all()
    return render(request,'index.html',{'userdata':userdata})
def home(request):
    return render(request,'home.html')
def userDetailsAdd(request):
    name=request.POST['name']
    email=request.POST['email']
    UserDetail.objects.create(name=name,email=email).save()
    return redirect('/homeUrl')
def edituser(request,id):
    userdata=UserDetail.objects.get(id=id)
    return render(request,'edituser.html',{'userdata':userdata})
def userDetailsUpdate(request,id):
    name=request.POST['name']
    email=request.POST['email']
    UserDetail.objects.filter(id=id).update(name=name,email=email)
    return redirect('/')
def userDetailsDelete(request,id):
    UserDetail.objects.filter(id=id).delete()
    return redirect('/')