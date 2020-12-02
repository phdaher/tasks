from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def hello(request):
    return HttpResponse("Hello, world. You're at the tasks model.")


def getTasks(request):
    tasks = Task.objects.all()
    task_serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(task_serializer.data, safe=False)

@csrf_exempt
def createTask(request):
    task_data = JSONParser().parse(request)
    task_serializer = TaskSerializer(data=task_data)
    if task_serializer.is_valid():
        task_serializer.save()
        return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
