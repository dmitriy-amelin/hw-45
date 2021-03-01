from django.shortcuts import render

from to_do_list.models import ToDoList, status_choices


def index_view(request):
    tasks = ToDoList.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context)


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {"choices": status_choices})

