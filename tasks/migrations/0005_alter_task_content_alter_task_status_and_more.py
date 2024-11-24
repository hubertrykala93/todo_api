# Generated by Django 5.1.3 on 2024-11-24 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_alter_task_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task", name="content", field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tasks.taskstatus",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="taskpriority",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="taskstatus",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]