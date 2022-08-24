from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField() #  models.CharField(max_length=255)
    thumb = models.ImageField(upload_to ='media/uploads/%Y/%m/%d/', null=True)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField()

    #  Retorna o nome do Titulo para a listagem no /admin
    def __str__(self):
        return self.title
