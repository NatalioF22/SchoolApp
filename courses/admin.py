from django.contrib import admin
from .models import *

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'credits', 'is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('code', 'name', 'description')


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'minimum_credits', 'department')
    search_fields = ('name', 'code', 'description', 'department__name')
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

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_name')
    search_fields = ('name','code_name')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'chairperson')
    search_fields = ('name', 'code')
    list_filter = ('chairperson',)

@admin.register(CourseOutline)
class CourseOutlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'created_by', 'created_at')
    search_fields = ('title', 'department__name')
    list_filter = ('department', 'created_by', 'created_at')

    

@admin.register(DepartmentComment)
class DepartmentCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'created_at')
    search_fields = ('user__username', 'department__name')
    list_filter = ('department', 'user', 'created_at')

@admin.register(DepartmentReview)
class DepartmentReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'rating', 'created_at')
    search_fields = ('user__username', 'department__name')
    list_filter = ('department', 'user', 'rating', 'created_at')