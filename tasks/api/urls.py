from django.urls import path
from . import views as api_tasks_views

urlpatterns = [
    path("api/v1/taskstatuses", api_tasks_views.TaskStatusListCreateAPIView.as_view(), name="taskstatuses"),
    path("api/v1/taskstatuses/<int:pk>", api_tasks_views.TaskStatusRetrieveUpdateDeleteAPIView.as_view(),
         name="taskstatus-update-delete"),
    path("api/v1/taskpriorities", api_tasks_views.TaskPriorityListCreateAPIView.as_view(), name="taskpriorities"),
    path("api/v1/taskpriorities/<int:pk>", api_tasks_views.TaskPriorityRetrieveUpdateDeleteAPIView.as_view(),
         name="taskpriority-update-delete")
]
