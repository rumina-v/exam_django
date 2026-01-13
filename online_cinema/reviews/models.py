from django.db import models
from django.contrib.auth.models import User
from movies.models import BaseModel 

class Review(BaseModel): 
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='reviews', verbose_name="Фильм")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField(blank=True, verbose_name="Отзыв")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Рейтинг")

    def __str__(self):
        return f"Отзыв к {self.movie.title} от {self.user.username}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"