from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("save-task/", save_task, name="save-task"),
    path("get-all-tasks/", get_all_tasks, name="get-all-tasks"),
    path("get-done-tasks/", get_done_tasks, name="get-done-tasks"),
    path("get-pending-tasks/", get_pending_tasks, name="get-pending-tasks"),
]
