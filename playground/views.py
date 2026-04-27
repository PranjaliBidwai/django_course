from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    #return HttpResponse("Hello, World!")
    return render(request, "hello.html", {'name': 'Django'})

# Create your views here.
# pull from db and render template
