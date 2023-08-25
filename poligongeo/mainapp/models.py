from django.db import models


class CallRequest(models.Model):

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    first_name = models.CharField(max_length=128, verbose_name='Имя')
    phone = models.CharField(max_length=128, verbose_name='Телефон')
    email = models.CharField(max_length=128, verbose_name='Email')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return str(self.id)