from django.contrib import admin
from .models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'availability_status', 'location')
    search_fields = ('title', 'author')
    list_filter = ('availability_status', 'publication_year')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'publisher', 'availability_status', 'location')
    search_fields = ('title', 'author', 'publisher')
    list_filter = ('availability_status', 'publication_year')

@admin.register(StudySpace)
class StudySpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity', 'availability')
    search_fields = ('name', 'location')
    list_filter = ('availability',)

@admin.register(TutoringService)
class TutoringServiceAdmin(admin.ModelAdmin):
    list_display = ('subject_area', 'tutor', 'location')
    search_fields = ('subject_area', 'tutor__username')
    list_filter = ('subject_area',)

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'application_deadline')
    search_fields = ('title', 'company')
    list_filter = ('application_deadline',)

@admin.register(CareerEvent)
class CareerEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location')
    search_fields = ('name', 'location')
    list_filter = ('date',)

@admin.register(StudentOrganization)
class StudentOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'contact_email')
    search_fields = ('name', 'category')
    list_filter = ('category',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location', 'organizer')
    search_fields = ('name', 'location', 'organizer__username')
    list_filter = ('date',)

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('route_number',)
    search_fields = ('route_number',)

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'location')
    search_fields = ('name', 'code', 'location')