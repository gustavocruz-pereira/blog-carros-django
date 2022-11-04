from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    thumb = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True,
                                    null=True)
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

