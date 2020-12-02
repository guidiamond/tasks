from django.urls import path

from django.http import HttpResponseNotAllowed

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("get_all", views.get_tasks, name="get all tasks"),
    path("deleteTasks", views.delete_tasks, name="delete all tasks"),
    path("postTask", views.post_task, name="create new task"),
]
