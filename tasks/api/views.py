from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tasks.models import TaskStatus, TaskPriority, Task
from .serializers import TaskStatusSerializer, TaskPrioritySerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound


class TaskStatusListCreateAPIView(ListCreateAPIView):
    def get_queryset(self):
        return TaskStatus.objects.all().order_by("id")

    def get_serializer_class(self):
        return TaskStatusSerializer

    def get(self, request, *args, **kwargs):
        objects = self.get_queryset()
        serializer = self.get_serializer(objects, many=True)

        return Response(
            data={
                "message": "Task Statuses retrieved successfully.",
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()

            except IntegrityError:
                return Response(
                    data={
                        "message": f"Task Status named '{serializer.data.get('name')}' already exists.",
                        "success": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "message": "Task Status has been successfully created.",
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data={
                    "message": "Failed to create a new task status.",
                    "success": False,
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class TaskStatusRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return TaskStatus.objects.all()

    def get_serializer_class(self):
        return TaskStatusSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            serializer = self.get_serializer(
                instance=instance,
            )

            return Response(
                data={
                    "message": f"Task Status with ID '{instance.pk}' has been successfully retrieved.",
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except NotFound:
            return Response(
                data={
                    "message": f"Task Status with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            serializer = self.get_serializer(
                instance=instance,
                data=request.data
            )

            if serializer.is_valid():
                serializer.save()

                return Response(
                    data={
                        "message": f"Task Status with ID '{instance.pk}' has been successfully updated.",
                        "success": True,
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    data={
                        "message": "Failed to create a new task status.",
                        "success": False,
                        "data": serializer.data,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except NotFound:
            return Response(
                data={
                    "message": f"Task Status with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            return Response(
                data={
                    "message": f"Task Status with ID '{kwargs.get('pk')}' has been successfully deleted.",
                    "success": True,
                },
                status=status.HTTP_204_NO_CONTENT,
            )

        except TaskStatus.DoesNotExist:
            return Response(
                data={
                    "message": f"Task Status with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                data={
                    "message": str(e),
                    "success": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class TaskPriorityListCreateAPIView(ListCreateAPIView):
    def get_queryset(self):
        return TaskPriority.objects.all().order_by("id")

    def get_serializer_class(self):
        return TaskPrioritySerializer

    def get(self, request, *args, **kwargs):
        objects = self.get_queryset()
        serializer = self.get_serializer(objects, many=True)

        return Response(
            data={
                "message": "Task Priorities retrieved successfully.",
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()

            except IntegrityError:
                return Response(
                    data={
                        "message": f"Task Priority named '{serializer.data.get('name')}' already exists.",
                        "success": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "message": "Task Priority has been successfully created.",
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data={
                    "message": "Failed to create a new task priority.",
                    "success": False,
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class TaskPriorityRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return TaskPriority.objects.all()

    def get_serializer_class(self):
        return TaskPrioritySerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            serializer = self.get_serializer(
                instance=instance,
            )

            return Response(
                data={
                    "message": f"Task Priority with ID '{instance.pk}' has been successfully retrieved.",
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except NotFound:
            return Response(
                data={
                    "message": f"Task Priority with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            serializer = self.get_serializer(
                instance=instance,
                data=request.data
            )

            if serializer.is_valid():
                serializer.save()

                return Response(
                    data={
                        "message": f"Task Priority with ID '{instance.pk}' has been successfully updated.",
                        "success": True,
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    data={
                        "message": "Failed to create a new task priority.",
                        "success": False,
                        "data": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except NotFound:
            return Response(
                data={
                    "message": f"Task Priority with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            return Response(
                data={
                    "message": f"Task Priority with ID '{kwargs.get('pk')}' has been successfully deleted.",
                    "success": True,
                },
                status=status.HTTP_204_NO_CONTENT,
            )

        except TaskPriority.DoesNotExist:
            return Response(
                data={
                    "message": f"Task Priority with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                data={
                    "message": str(e),
                    "success": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class TaskListCreateAPIView(ListCreateAPIView):
    def get_queryset(self):
        return Task.objects.all()

    def get_serializer_class(self):
        return TaskSerializer

    def get(self, request, *args, **kwargs):
        objects = self.get_queryset()
        serializer = self.get_serializer(objects, many=True)

        return Response(
            data={
                "message": "Tasks retrieved successfully." if len(serializer.data) > 0 else "No tasks found.",
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()

            except IntegrityError:
                return Response(
                    data={
                        "message": f"Task named '{serializer.data.get('title')}' already exists.",
                        "success": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "message": "Task has been successfully created.",
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data={
                    "message": "Failed to create a new task.",
                    "success": False,
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class TaskRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Task.objects.all()

    def get_serializer_class(self):
        return TaskSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            serializer = self.get_serializer(
                instance=instance,
            )

            return Response(
                data={
                    "message": f"Task with ID '{instance.pk}' has been successfully retrieved.",
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except NotFound:
            return Response(
                data={
                    "message": f"Task with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            serializer = self.get_serializer(
                instance=instance,
                data=request.data
            )

            if serializer.is_valid():
                serializer.save()

                return Response(
                    data={
                        "message": f"Task with ID '{instance.pk}' has been successfully updated.",
                        "success": True,
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    data={
                        "message": "Failed to create a new task.",
                        "success": False,
                        "data": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except NotFound:
            return Response(
                data={
                    "message": f"Task with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            return Response(
                data={
                    "message": f"Task with ID '{kwargs.get('pk')}' has been successfully deleted.",
                    "success": True,
                },
                status=status.HTTP_204_NO_CONTENT,
            )

        except TaskPriority.DoesNotExist:
            return Response(
                data={
                    "message": f"Task with ID '{kwargs.get('pk')} does not exists.",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                data={
                    "message": str(e),
                    "success": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
