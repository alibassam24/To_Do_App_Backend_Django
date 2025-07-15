from os import name

from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("save-task/", save_task, name="save-task"),
    path("get-all-tasks/", get_all_tasks, name="get-all-tasks"),
    path("get-done-tasks/", get_done_tasks, name="get-done-tasks"),
    path("get-pending-tasks/", get_pending_tasks, name="get-pending-tasks"),
    path("delete-task/<str:name>",delete_task,name="delete-task"),
    path("task-completed/<int:id>",task_completed,name="task-completed"),
    path("task-due/<int:id>",task_due,name="task-due"),
    path("update-task/<int:id>",update_task,name='update-task')
]
