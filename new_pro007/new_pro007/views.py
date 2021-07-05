from django.http import HttpResponse
from django.shortcuts import render


def khan(request):
    return render(request,"index.html")
    

