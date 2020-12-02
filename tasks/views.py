from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from tasks.models import Task
from tasks.serializer import TaskSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def get_tasks(request):
    if request.method == "GET":
        task = TaskSerializer(Task.objects.all(), many=True)
        return JsonResponse(task.data, safe=False)


@api_view(["DELETE"])
def delete_tasks(request):
    if request.method == "DELETE":
        Task.objects.all().delete()
        return JsonResponse({"Status": "REMOVED SUCCESSFULLY!"}, status=200)


@api_view(["POST"])
def create_new_task(request):
    if request.method == "POST":
        new_task = JSONParser().parse(request)
        serializer = TaskSerializer(data=new_task)

        status = 404  # bad request
        # check if request matches schema
        if serializer.is_valid():
            serializer.save()
            status = 201  # created
        return JsonResponse(serializer.errors, status=status)
