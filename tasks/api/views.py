from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tasks.models import TaskStatus, TaskPriority
from .serializers import TaskStatusSerializer, TaskPrioritySerializer
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
                "success": "Task Statuses retrieved successfully.",
                "objects": serializer.data,
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
                        "error": f"Task Status named '{serializer.data.get('name')}' already exists.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "success": "Task Status has been successfully created.",
                    "object": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data=serializer.errors,
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
                    "success": f"Task Status with ID '{instance.pk}' has been successfully retrieved.",
                    "object": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except NotFound:
            return Response(
                data={
                    "error": f"Task Status with ID '{kwargs.get('pk')} does not exists.",
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
                        "success": f"Task Status with ID '{instance.pk}' has been successfully updated.",
                        "object": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except NotFound:
            return Response(
                data={
                    "error": f"Task Status with ID '{kwargs.get('pk')} does not exists.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            return Response(
                data={
                    "success": f"Task Status with ID '{kwargs.get('pk')}' has been successfully deleted.",
                },
                status=status.HTTP_204_NO_CONTENT,
            )

        except TaskStatus.DoesNotExist:
            return Response(
                data={
                    "error": f"Task Status with ID '{kwargs.get('pk')} does not exists.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                data={
                    "error": str(e),
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
                "success": "Task Priorities retrieved successfully.",
                "objects": serializer.data,
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
                        "error": f"Task Priority named '{serializer.data.get('name')}' already exists.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "success": "Task Priority has been successfully created.",
                    "object": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data=serializer.errors,
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
                    "success": f"Task Priority with ID '{instance.pk}' has been successfully retrieved.",
                    "object": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except NotFound:
            return Response(
                data={
                    "error": f"Task Priority with ID '{kwargs.get('pk')} does not exists.",
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
                        "success": f"Task Priority with ID '{instance.pk}' has been successfully updated.",
                        "object": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except NotFound:
            return Response(
                data={
                    "error": f"Task Priority with ID '{kwargs.get('pk')} does not exists.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            return Response(
                data={
                    "success": f"Task Priority with ID '{kwargs.get('pk')}' has been successfully deleted.",
                },
                status=status.HTTP_204_NO_CONTENT,
            )

        except TaskPriority.DoesNotExist:
            return Response(
                data={
                    "error": f"Task Priority with ID '{kwargs.get('pk')} does not exists.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                data={
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
