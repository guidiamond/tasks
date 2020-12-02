from django.http import HttpResponseNotAllowed
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_all", views.get_tasks, name="all tasks listing"),
    path("delete_all", views.delete_tasks, name="all tasks removal"),
    path("create", views.post_task, name="new task creation"),
]
