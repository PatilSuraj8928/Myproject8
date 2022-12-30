from django.shortcuts import render

# Create your views here.
def html1(request):
    d={'name':'Patil Suraj'}
    return render(request,'html1.html',context=d)