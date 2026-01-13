from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True

class Movie(BaseModel):  
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    director = models.CharField(max_length=100, verbose_name="Режиссёр")
    genre = models.CharField(max_length=50, blank=True, verbose_name="Жанр")
    description = models.TextField(blank=True, verbose_name="Описание")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    poster = models.ImageField(upload_to='posters/', blank=True, null=True, verbose_name="Постер")

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"