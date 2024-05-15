from django.shortcuts import render
from courses.models import *

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def courses(request):
    majors_list = Major.objects.all()
    return render(request, "courses.html", {'majors_list':majors_list}) 

