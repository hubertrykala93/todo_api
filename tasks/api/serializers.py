from rest_framework import serializers
from tasks.models import TaskStatus, TaskPriority, Task


class TaskStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=2,
        max_length=100,
        error_messages={
            "required": "Task Status is required.",
            "blank": "Task Status is required.",
            "min_length": "Task Status must consist of at least 2 characters.",
            "max_length": "Task Status must consist of no more than 100 characters.",
        },
    )

    class Meta:
        model = TaskStatus
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TaskStatusSerializer, self).__init__(*args, **kwargs)

        if self.context.get("view").__class__.__name__ == "TaskStatusRetrieveUpdateDeleteAPIView":
            self.fields["name"].required = False


class TaskPrioritySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=2,
        max_length=100,
        error_messages={
            "required": "Task Status is required.",
            "blank": "Task Status is required.",
            "min_length": "Task Status must consist of at least 2 characters.",
            "max_length": "Task Status must consist of no more than 100 characters.",
        },
    )

    class Meta:
        model = TaskPriority
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TaskPrioritySerializer, self).__init__(*args, **kwargs)

        if self.context.get("view").__class__.__name__ == "TaskPriorityRetrieveUpdateDeleteAPIView":
            self.fields["name"].required = False


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        min_length=5,
        max_length=100,
        error_messages={
            "required": "Title is required.",
            "blank": "Title is required.",
            "min_length": "The title must consist of at least 5 characters.",
            "max_length": "The title must consist of no more than 100 characters.",
        },
    )

    content = serializers.CharField(
        min_length=10,
        max_length=255,
        error_messages={
            "required": "Content is required.",
            "blank": "Content is required.",
            "min_length": "The content must consist of at least 10 characters.",
            "max_length": "The content must consist of no more than 255 characters.",
        },
    )

    status = serializers.SlugRelatedField(
        error_messages={
            "required": "Task Status is required.",
            "does_not_exist": f"Task Status does not exists. Available task statuses are 'Pending', 'In Progress', 'Complete'.",
        },
        queryset=TaskStatus.objects.all(),
        slug_field="name",
    )

    due_date = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        error_messages={
            "required": "Due Date is required.",
            "null": "Due Date is required.",
            "blank": "Due Date is required.",
            "invalid": "The provided date format is incorrect. The correct format is YYYY-MM-DD HH:MM:SS.",
        },
    )

    priority = serializers.SlugRelatedField(
        error_messages={
            "required": "Task Priority is required.",
            "does_not_exist": f"Task Priority does not exists. Available task priorities are 'High', 'Medium', 'Low'.",
        },
        queryset=TaskPriority.objects.all(),
        slug_field="name",
    )

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {
            "created_at": {
                "format": "%Y-%m-%d %H:%M:%S",
            },
            "updated_at": {
                "format": "%Y-%m-%d %H:%M:%S",
            },
        }

    def __init__(self, *args, **kwargs):
        super(TaskSerializer, self).__init__(*args, **kwargs)

        if self.context.get("view").__class__.__name__ == "TaskRetrieveUpdateDeleteAPIView":
            self.fields["title"].required = False
            self.fields["content"].required = False
            self.fields["status"].required = False
            self.fields["due_date"].required = False
            self.fields["priority"].required = False
