from django.db import models
from django.contrib.auth.models import User


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Toвap')
    content = models.TextField(null=True, blank=True, verbose_name='Onиcaниe')
    price = models.FloatField(null=True, blank=True, verbose_name='Цeнa')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta :
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published'] 

    def title_and_price(self) :
        if self.price :
            return '%s (%.2f)' % (self.title, self.price)
        else:
            return self.title
    title_and_price.short_description = 'Название и цена'


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Haзвaниe')

    def __str__(self):
        return self.name

    class Meta :
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name'] 

    def get_absolute_url(self) :
        return f'/bboard/{self.pk}/'