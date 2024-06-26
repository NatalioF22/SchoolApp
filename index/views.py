from django.shortcuts import render
from django.db.models import Avg
from courses.models import *
from campus_resources.models import Event
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def courses(request):
    majors_list = Major.objects.all()
    return render(request, "courses.html", {'majors_list':majors_list}) 

def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})

def events(request):
    events = Event.objects.all()
    return render(request, "events.html", {'events':events})

def event_details(request, pk):
    event = get_object_or_404(Event, id=pk)
    return render(request, "event-details.html", {'event':event})



def department_details(request, pk):
    department = get_object_or_404(Department, pk=pk)
    reviews = department.reviews.all()
    
    # Calculate the average rating manually
    total_rating = sum(review.rating for review in reviews)
    num_reviews = reviews.count()
    if num_reviews > 0:
        avg_rating = total_rating / num_reviews
    else:
        avg_rating = 0

    for review in reviews:
        review.star_range = range(review.rating)
        review.empty_star_range = range(5 - review.rating)

    context = {
        'department': department,
        'reviews': reviews,
        'avg_rating': avg_rating,
    }
    return render(request, 'department_details.html', context)
