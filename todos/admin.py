from django.contrib import admin

from todos.models import Task, TaskList


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    """Admin for task lists."""

    list_display = ['title', 'description', 'undone_count']
    search_fields = ['title', 'description']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin for tasks."""

    list_display = ['title', 'description', 'done']
    list_filter = ['task_list', 'done']
    search_fields = ['title', 'description', 'task_list__title']