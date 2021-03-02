from django.urls import path

from to_do_list.views import index_view, task_create_view, task_view

urlpatterns = [
    path('', index_view),
    path('task/add/', task_create_view),
    path('task/', task_view),
]
