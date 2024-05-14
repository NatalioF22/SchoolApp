from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Person, Student, Professor

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'DOB', 'race', 'sex', 'city', 'state', 'country')
    list_filter = ('sex', 'race', 'state', 'country')
    search_fields = ('first_name', 'last_name', 'phone_number', 'city', 'state', 'country')

@admin.register(Student)
class StudentAdmin(PersonAdmin):
    list_display = PersonAdmin.list_display + ('level', 'status', 'student_type', 'campus', 'major', 'gpa', 'credits_earned', 'get_age')
    list_filter = PersonAdmin.list_filter + ('level', 'status', 'student_type', 'campus', 'major')
    search_fields = PersonAdmin.search_fields + ('major__name', 'minor__name', 'classes_taking__name', 'classes_took__name')
    readonly_fields = ('get_age',)

    def get_age(self, obj):
        return obj.get_age()

    get_age.short_description = 'Age'

@admin.register(Professor)
class ProfessorAdmin(PersonAdmin):
    list_display = PersonAdmin.list_display + ('title', 'department', 'hire_date', 'get_email')
    list_filter = PersonAdmin.list_filter + ('title', 'department')
    search_fields = PersonAdmin.search_fields + ('department__name',)