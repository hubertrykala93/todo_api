from rest_framework import serializers
from tasks.models import TaskStatus, TaskPriority


class TaskStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        allow_blank=True,
    )

    class Meta:
        model = TaskStatus
        fields = "__all__"

    def validate_name(self, name):
        if name == "":
            raise serializers.ValidationError(
                detail="Task Status name is required.",
            )

        if len(name) < 2:
            raise serializers.ValidationError(
                detail="Task Status must consist of at least 2 characters.",
            )

        if len(name) > 100:
            raise serializers.ValidationError(
                detail="Task Status must consist of no more than 100 characters.",
            )

        return name


class TaskPrioritySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        allow_blank=True,
    )

    class Meta:
        model = TaskPriority
        fields = "__all__"

    def validate_name(self, name):
        if name == "":
            raise serializers.ValidationError(
                detail="Task Priority name is required.",
            )

        if len(name) < 2:
            raise serializers.ValidationError(
                detail="Task Priority must consist of at least 2 characters.",
            )

        if len(name) > 100:
            raise serializers.ValidationError(
                detail="Task Priority must consist of no more than 100 characters.",
            )

        return name
