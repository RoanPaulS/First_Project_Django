from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    message = "<h1>Hi Paul How are You</h1>"
    return HttpResponse(message)

