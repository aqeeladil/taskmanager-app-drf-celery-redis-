from django.urls import path
from .views import TaskListCreateAPIView, task_form_view

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('task-form/', task_form_view, name='task-form-view')
]
