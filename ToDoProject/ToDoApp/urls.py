from django.urls import path
from .views import *
from django.contrib import admin
urlpatterns=[
    path('save-task/',save_task,name='save-task'),
]