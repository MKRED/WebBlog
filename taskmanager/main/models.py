from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField('Название', max_length=50)
    discription = models.TextField('Описание')

    def __str__(self):
        return self.title

class Comment(models.Model):
    father_post = models.ForeignKey(Post, related_name='Пост', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, related_name='Автор', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Пост: {} - Коммент {}'.format(self.father_post, self.body)
