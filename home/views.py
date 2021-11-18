from django.shortcuts import render,HttpResponse
import numpy as np
import pickle
from home.test import fun

# model logic 

# output vatriable 

# Create your views here.
def home(request):
    
    
    return render(request,"home/home.html")  # output variable passing 
    
def predict(request):
    if request.method=="POST":
        inn_=request.POST['inns']
        overi_=request.POST['overi']
        balli_=request.POST['balli']
        overf_=request.POST['overf']
        ballf_=request.POST['ballf'] 
        inn_=(int(inn_))
        overi_=int(overi_)
        balli_=int(balli_)
        overf_=int(overf_)
        ballf_=int(ballf_)
        ANS=fun(inn_,overi_,balli_,overf_,ballf_)    
        d={'ans':ANS}
    return render(request,"home/predict.html",d)