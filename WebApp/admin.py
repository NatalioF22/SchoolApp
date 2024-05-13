from django.contrib import admin
from .models import CustomUser, Student, Professor, Subject

class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'level', 'class_type', 'status', 'student_type', 'campus', 'advisor')
    search_fields = ('first_name', 'last_name', 'level', 'class_type', 'status', 'student_type', 'campus')
    list_filter = ('level', 'class_type', 'status', 'student_type', 'campus')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(advisor__user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'advisor' and not request.user.is_superuser:
            kwargs['queryset'] = Professor.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.advisor.user != request.user and not request.user.is_superuser:
            return False
        return True

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'status', 'professor_type')
    search_fields = ('first_name', 'last_name', 'status', 'professor_type')
    list_filter = ('status', 'professor_type')
    filter_horizontal = ('classes_teaching',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser:
            return False
        return True

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('CRN', 'title', 'code', 'section', 'credits', 'professor')
    search_fields = ('CRN', 'title', 'code', 'section', 'professor__first_name', 'professor__last_name')
    list_filter = ('code', 'section', 'professor')
    filter_horizontal = ('students',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'professor' and not request.user.is_superuser:
            kwargs['queryset'] = Professor.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(professor__user=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.professor.user != request.user and not request.user.is_superuser:
            return False
        return True

admin.site.register(CustomUser)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Subject, SubjectAdmin)