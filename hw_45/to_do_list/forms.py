from django import forms

from to_do_list.models import ToDoList


class TaskForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ('author', 'status', 'description', 'full_description', 'date_of_completion')


class TaskDeleteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label='Введите название задачи, чтобы удалить её')
