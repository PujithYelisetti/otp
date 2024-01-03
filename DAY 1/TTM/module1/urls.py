from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('hello/',hello,name = 'hello'),
    path('',newhomepage,name ='newhomepage'),
    path('travelpackage/',travelpackage,name="travelpackage"),
    path('print/',print1,name="print"),
    path('print_to_console1/',print_to_co nsole,name='print_to_console1'),
path('callrandomotp/',randomcall,name='randomcall'),
    path('printotpconsole/',RandomOTPgenerator,name='RandomOTPgenerator')
]