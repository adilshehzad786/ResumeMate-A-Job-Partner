from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html', {})

def verify(request):
    return render(request, 'home/googled2ab8cb98bcc7215.html', {})
