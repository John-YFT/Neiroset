from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Дата')

    def __str__(self):
        return self.name


class Bb(models.Model):
    image_rez = models.ImageField(null = True, verbose_name='Images_rez')
    image = models.ImageField(null = True, verbose_name='Images')
    published = models.DateTimeField(null = True, auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT,  verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rez(models.Model):
    image_rez = models.ImageField(null = True, verbose_name='Images_rez')
