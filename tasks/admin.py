from django.contrib import admin
from .models import TaskPriority, TaskStatus, Task


@admin.register(TaskPriority)
class AdminTaskPriority(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    fields = ["name"]


@admin.register(TaskStatus)
class AdminTaskStatus(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    fields = ["name"]


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = [
        "id",
        "formatted_created_at",
        "formatted_updated_at",
        "title",
        "slug",
        "content",
        "status",
        "formatted_due_date",
        "priority",
    ]
    fields = [
        "title",
        "content",
        "due_date",
        "priority",
    ]

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def formatted_updated_at(self, obj):
        if obj.updated_at:
            return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_updated_at.short_description = "Updated At"

    def formatted_due_date(self, obj):
        if obj.due_date:
            return obj.due_date.strftime("%Y-%m-%d %H:%M:%S")

    formatted_due_date.short_description = "Due Date"
