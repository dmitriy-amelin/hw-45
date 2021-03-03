from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    elif request.method == 'POST':
        description = request.POST.get("description")
        full_description = request.POST.get("full_description")
        status = request.POST.get("status")
        author = request.POST.get("author")
        date_of_completion = request.POST.get("date_of_completion")

        task = ToDoList.objects.create(
            description=description,
            full_description=full_description,
            status=status,
            author=author,
            date_of_completion=date_of_completion
        )

        return redirect('task-view', pk=task.id)


def task_view(request, pk):
    task = get_object_or_404(ToDoList, id=pk)
    return render(request, 'task_view.html', context={'task': task})
