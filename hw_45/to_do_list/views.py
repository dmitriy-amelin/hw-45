from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from to_do_list.forms import TaskForm
from to_do_list.models import ToDoList, status_choices


def index_view(request):
    tasks = ToDoList.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context)


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form, 'choices': status_choices})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = ToDoList.objects.create(
                description=form.cleaned_data.get("description"),
                full_description=form.cleaned_data.get("full_description"),
                status=form.cleaned_data.get("status"),
                author=form.cleaned_data.get("author"),
                date_of_completion=form.cleaned_data.get("date_of_completion")
            )
            return redirect('task-view', pk=task.id)
        return render(request, 'task_create.html', context={'form': form, 'choices': status_choices})


def task_view(request, pk):
    task = get_object_or_404(ToDoList, id=pk)
    return render(request, 'task_view.html', context={'task': task})


def task_update_view(request, pk):
    task = get_object_or_404(ToDoList, id=pk)

    if request.method == 'GET':
        form = TaskForm(initial={
            'author': task.author,
            'description': task.description,
            'full_description': task.full_description,
            'date_of_completion': task.date_of_completion,
            'status': task.status
        })
        return render(request, 'task_update.html', context={'form': form, 'task': task, "choices": status_choices})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = request.POST.get("description")
            task.full_description = request.POST.get("full_description")
            task.status = request.POST.get("status")
            task.author = request.POST.get("author")
            task.date_of_completion = request.POST.get("date_of_completion")
            task.save()
            return redirect('task-view', pk=task.id)

        return render(request, 'task_update.html', context={'form': form, 'task': task, "choices": status_choices})


def task_delete_view(request, pk):
    task = get_object_or_404(ToDoList, id=pk)

    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('task-list')
