import time
from celery import shared_task

@shared_task
def send_task_created_notification(task_id, task_title):
    print(f"Preparing to send notification for task {task_id}...")
    time.sleep(5)  # simulate some delay
    print(f"Notification: Task '{task_title}' has been created successfully!")
    return f"Notification sent for task {task_id}"
