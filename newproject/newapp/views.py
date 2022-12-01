from django.http import HttpResponse
from django.shortcuts import render
from . models import  b
from . models import forest
from . models import hillstation
from . models import founder
from . models import manager
from . models import travel
from . models import consultant
from . models import beach

# Create your views here.
def demo(request):
    
    obj=b.objects.all()
    ob1=forest.objects.all()
    ob2=hillstation.objects.all()
    ob3=founder.objects.all()
    ob4=manager.objects.all()
    ob5=travel.objects.all()
    ob6=consultant.objects.all()
    ob7=beach.objects.all()
    
    
    return  render(request,"index.html",{'result':obj,'res1':ob1,'res2':ob2,'res3':ob3,'res4':ob4,'res5':ob5,'res6':ob6,'res7':ob7})

#def eg1(request):
    #return render(request,"about.html")
#def eg2(request):
    #return HttpResponse("helloo am contact")

#def demo8(request):
    #name="india"
    #return render (request,'index1.html',{'obj':name})
#def demo9(request):
    #name="india"
    #return render (request,'index2.html',{'obj':name})
#*args#def addition(request):
   # a=int(request.GET['num1'])
   # b=int(request.GET['num2'])""
    #c=a+b
   # d=a-b
  #  e=a*b
 #   f=a/b
####   return render(request,'result.html',{'result':c,'resul':d,'resu':e,'res':f})

    