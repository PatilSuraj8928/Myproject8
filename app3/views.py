from django.shortcuts import render

# Create your views here.
def html2(request):
    d={'mobile':[9900088,783452]}
    return render(request,'html2.html',d)