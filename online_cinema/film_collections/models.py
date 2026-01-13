from django.db import models
from django.contrib.auth.models import User
from movies.models import BaseModel

class Collection(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    name = models.CharField(max_length=100, verbose_name="Название подборки")
    description = models.TextField(blank=True, verbose_name="Описание")
    movies = models.ManyToManyField('movies.Movie', verbose_name="Фильмы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"