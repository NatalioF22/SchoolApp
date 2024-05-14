from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'application_date', 'status', 'major')
    list_filter = ('status', 'application_date', 'major')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')
    readonly_fields = ('application_date',)
    fieldsets = (
        (None, {
            'fields': ('user', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'date_of_birth', 'gender')
        }),
        ('Application Details', {
            'fields': ('application_date', 'status', 'reviewed_by', 'major', 'transcript', 'essay')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.reviewed_by = request.user
        super().save_model(request, obj, form, change)