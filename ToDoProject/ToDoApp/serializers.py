from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import task


class TaskSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model=task
        fields='__all__'
        read_only_fields=['id']

