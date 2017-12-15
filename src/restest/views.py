from django.shortcuts import render
from rest_framework import viewsets

from .models import Task
from .Serializers import TaskSerializer

class TaskViewSet(viewsets.ViewSet):

    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializer
