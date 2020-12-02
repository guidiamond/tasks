from django.urls import path

# import logger
from django.http import HttpResponseNotAllowed

from . import views


# extracted from: https://stackoverflow.com/questions/19096227/how-to-discriminate-based-on-http-method-in-django-urlpatterns
# def method_dispatch(**table):
#     def invalid_method(request, *args, **kwargs):
#         logger.warning(
#             "Method Not Allowed (%s): %s",
#             request.method,
#             request.path,
#             extra={"status_code": 405, "request": request},
#         )
#         return HttpResponseNotAllowed(table.keys())
#
#     def d(request, *args, **kwargs):
#         handler = table.get(request.method, invalid_method)
#         return handler(request, *args, **kwargs)
#
#     return d


urlpatterns = [
    path("", views.index, name="index"),
    path("getTasks", views.get_tasks, name="get all tasks"),
    path("deleteTasks", views.delete_tasks, name="delete all tasks"),
    path("postTask", views.post_task, name="create new task"),
]
