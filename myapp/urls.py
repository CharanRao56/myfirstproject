from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('',home,name='home'),
    path('course/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('requestcallback/',requestCallBack,name='requestCallBack'),
]