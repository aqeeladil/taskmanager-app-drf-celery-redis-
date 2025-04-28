from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_task_created_notification
from django.shortcuts import render

# This is a simple Django view (not DRF).
def task_form_view(request):
    return render(request, 'tasks/task_form.html')


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    # perform_create() is called automatically when Django saves a new object.
    def perform_create(self, serializer):
        task = serializer.save()
        # Trigger Celery task
        # After saving the task, we immediately call .delay() to send it to Celery worker.
        send_task_created_notification.delay(task.id, task.title)
