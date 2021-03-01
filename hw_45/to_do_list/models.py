from django.db import models


class ToDoList(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    description = models.TextField(max_length=3000, null=False, blank=False)
    status = models.CharField(max_length=300, null=False, blank=False, default='New', verbose_name='Статус')
    date_of_completion = models.DateField(auto_now_add=False,
                                          editable=True, null=True, blank=True, verbose_name='Дата выполнения')

    class Meta:
        db_table = 'to_do_list'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.description}: {self.status}, {self.date_of_completion}'
