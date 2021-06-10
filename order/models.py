from django.db import models
from django.urls import reverse


class Order(models.Model):
    date = models.DateTimeField(verbose_name='Дата приказа')
    number = models.CharField(max_length=20, verbose_name='Номер приказа')
    title = models.CharField(max_length=150, verbose_name='Название приказа')
    text = models.TextField(verbose_name='Текст приказа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_view', kwargs={"news_id": self.pk})

    class Meta:
        verbose_name = 'Приказ по кадрам'
        verbose_name_plural = 'Приказы по кадрам'
        ordering = ['-date']
