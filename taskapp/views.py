from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            self.dispatch
            return TaskListSerializer
        return TaskDetailSerializer

    