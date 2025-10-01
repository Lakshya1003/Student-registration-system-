from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome to the Student Registration System")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("My name is lakshya \n This is my first django project")


def contact(request):
    return HttpResponse("Contact us at: test_email@gmail.com")