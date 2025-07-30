"""Admin configuration for API app."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Custom admin class for TaskModel."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
