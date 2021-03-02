from django.urls import path

from to_do_list.views import index_view, task_create_view, task_view

urlpatterns = [
    path('', index_view, name='task-list'),
    path('task/add/', task_create_view, name='task-add'),
    path('task/<int:pk>', task_view, name='task-view'),
]
