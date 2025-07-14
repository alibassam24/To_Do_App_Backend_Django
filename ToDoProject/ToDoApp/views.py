from django.shortcuts import render
from rest_framework import  views, response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerialzer


# Create your views here.
"""
{
    "name":"Task 1",
    "date":"2025-07-06",
    "description":"Create first Django project"

}
"""
@api_view(['POST'])
def save_task(request):
    serializer=TaskSerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Success","Message":"Task Created","Data":serializer.data})
    else:
        return Response({"Status":"Failed","Message":"Data is not valid"})

@api_view(['GET'])
def get_all_tasks(request):
    t=Task.objects.all()
    
    serializer=TaskSerialzer(t, many=True)

    return Response({"Status":"Success","Data":serializer.data})