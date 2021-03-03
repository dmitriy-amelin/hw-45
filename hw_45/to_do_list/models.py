from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class ToDoList(models.Model):
    author = models.CharField(max_length=40, default='Unknown', verbose_name='Автор')
    description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(blank=True, verbose_name='Полное описание')
    status = models.CharField(max_length=40, choices=status_choices, default='new', verbose_name='Статус')
    date_of_completion = models.DateField(auto_now_add=False, default='',
                                          null=True, blank=True, verbose_name='Дата выполнения')

    class Meta:
        db_table = 'to_do_list'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.description}: {self.status}, {self.date_of_completion}'
