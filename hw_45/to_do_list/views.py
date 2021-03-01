from django.shortcuts import render

from to_do_list.models import ToDoList


def index_view(request):
    tasks = ToDoList.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context)
