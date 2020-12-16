from django.shortcuts import render

def home(request):
    return render(request,'Tutorial_Base.html')