from django.urls import path
from app3.views import *
app_name='something2'

urlpatterns=[ 
    path('html2/',html2,name='html2'),
    
]