from django.contrib import admin
from to_do_list.models import ToDoList


# Register your models here.


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_of_completion']
    list_filter = ['status']
    search_fields = ['status', 'description']
    fields = ['author', 'status', 'description', 'full_description', 'date_of_completion']


admin.site.register(ToDoList, ToDoListAdmin)
