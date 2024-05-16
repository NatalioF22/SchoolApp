#index.urls.py
from django.urls import path
from . import views


urlpatterns = [
      path("", views.home, name="home"),
      path("courses/", views.courses, name='courses_list'),
      path("about/", views.about, name='about'),
      path("contact/", views.contact, name="contact"),
      path("events/", views.events, name="events"),
      path("event/<int:pk>", views.event_details, name="event_details"),
      path("department/<int:pk>", views.department_details, name="department_details"),  # Add this line
]