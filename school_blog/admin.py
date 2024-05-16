# blog/admin.py

from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    # Add the 'image' field to the fieldsets
    fieldsets = (
        (None, {'fields': ('title', 'content', 'author', 'category', 'is_published')}),
        ('Media', {'fields': ('image',)}),
        ('Dates', {'fields': ('published_at',)}),
    )

    # Add the 'image_tag' method to display the image in the admin list view
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return ''
    image_tag.short_description = 'Image'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date_published', 'is_approved')
    list_filter = ('is_approved', 'post')
    search_fields = ('author__user__first_name', 'author__user__last_name', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"