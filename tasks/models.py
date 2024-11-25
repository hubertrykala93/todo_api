from django.db import models
from django.utils.text import slugify


class TaskStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = "Task Status"
        verbose_name_plural = "Task Statuses"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(TaskStatus, self).save(*args, **kwargs)


class TaskPriority(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = "Task Priority"
        verbose_name_plural = "Task Priorities"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(TaskPriority, self).save(*args, **kwargs)


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True)
    content = models.CharField(max_length=255)
    status = models.ForeignKey(to=TaskStatus, on_delete=models.SET_NULL, null=True)
    due_date = models.DateTimeField()
    priority = models.ForeignKey(to=TaskPriority, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Task, self).save(*args, **kwargs)
