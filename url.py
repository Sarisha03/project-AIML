from django.contrib import admin
from django.urls import path
from basic.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("dia/",dia,name="dia"),
   
    
]