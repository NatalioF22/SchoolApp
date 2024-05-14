from django.contrib import admin
from .models import Course, Major, Minor, Department

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'credits', 'is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('code', 'name', 'description')

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'minimum_credits')
    search_fields = ('name', 'code', 'description')
    filter_horizontal = (
        'core_courses',
        'required_courses',
        'core_skills',
        'core_seminars',
        'core_writing_speaking_intensive',
        'core_distribution',
        'core_additional_distribution',
        'program_requirements',
    )

@admin.register(Minor)
class MinorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'minimum_credits')
    search_fields = ('name', 'code', 'description')
    filter_horizontal = ('required_courses',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'chairperson')
    search_fields = ('name', 'code', 'description')