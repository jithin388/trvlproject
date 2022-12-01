from xml.dom.minidom import Document
from . import views
from django.urls import path,include
from newproject import settings
from   django.conf.urls.static import static


urlpatterns = [
    
    path('',views.demo,name='demo'),

    
    #path('eg1/',views.eg1,name='eg1'),
    #path('eg2/',views.eg2,name='eg2'),
    #path('demo8/',views.demo8,name='demo8'),
    #path('demo9/',views.demo,name='demo'),
    #path('add/',views.addition,name='addition'),
   
    
]

