from django.shortcuts import render
from rest_framework import response, views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
"""
{
    "name":"Task 1",
    "date":"2025-07-06",
    "description":"Create first Django project"

}
"""


@api_view(["POST"])
def save_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"Status": "Success", "Message": "Task Created", "Data": serializer.data}
        )
    else:
        return Response({"Status": "Failed", "Message": "Data is not valid"})


@api_view(["GET"])
def get_all_tasks(request):
    t = Task.objects.all()

    serializer = TaskSerializer(t, many=True)

    return Response({"Status": "Success", "Data": serializer.data})


@api_view(["GET"])
def get_done_tasks(request):
    t = Task.objects.filter(isDone=True)

    if t.exists():
        serializer = TaskSerializer(t, many=True)
        return Response({"Status": "Success", "Data": serializer.data})

    else:
        return Response({"Status": "Failed", "Message": "No Record Found"})


@api_view(["GET"])
def get_pending_tasks(request):
    t = Task.objects.filter(isDone=False)

    if t.exists():
        serializer = TaskSerializer(t, many=True)
        return Response({"Status": "Success", "Data": serializer.data})

    else:
        return Response({"Status": "Failed", "Message": "No Record Found"})


@api_view(["DELETE"])
def delete_task(request, name):
    try:
        t = Task.objects.get(name=name)
        t.delete()
        return Response({"Status": "Success", "Message": "Record Deleted Successfully"})
    except Task.DoesNotExist:
        return Response({"Status": "Failed", "Message": "Record Not Found"})


# mark task as done
@api_view(["POST"])
def task_completed(request, id):
    try:
        t = Task.objects.get(id=id)
        t.isDone = True
        serializer = TaskSerializer(t)
        t.save()
        return Response(
            {
                "Status": "Success",
                "Message": "Task Marked as Done",
                "Data": serializer.data,
            }
        )
    except Task.DoesNotExist:
        return Response({"Status": "Failed", "Message": "No such Task Found"})


@api_view(["POST"])
def task_due(request, id):
    try:
        t = Task.objects.get(id=id)
        t.isDone = False
        serializer = TaskSerializer(t)
        t.save()
        return Response(
            {
                "Status": "Success",
                "Message": "Task Marked as Due",
                "Data": serializer.data,
            }
        )
    except Task.DoesNotExist:
        return Response({"Status": "Failed", "Message": "No such Task Found"})


# Update data
# PUT,PATCH


@api_view(["PUT"])
def update_task(request, id):
    try:
        t = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({"Status": "Failed", "Message": "No Task with given id Found"})
    serializer = TaskSerializer(t, data=request.data)
    if serializer.is_valid():
        t.save()
        return Response(
            {"Status": "Success", "Message": "Task Updated", "Data": serializer.data}
        )
    else:
        return Response({"Status": "Failed", "Message": "Invalid Data"})
