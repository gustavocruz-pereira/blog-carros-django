from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to ='media/uploads/%Y/%m/%d/', null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField()

    #  Retorna o nome do Titulo para a listagem no /admin
    def __str__(self):
        return self.title
