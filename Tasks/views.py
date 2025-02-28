from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("Welcome to the Task Management System")

def Contact(request):
    return HttpResponse("This is Contact Page")

def Show_Task(request):
    return HttpResponse("This is Our Task Page")