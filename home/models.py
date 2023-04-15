from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    thumb = models.ImageField(upload_to='post_img/%Y/%m/%d', null=False)
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        slug = slugify(self.title)
        return reverse("model_detail", kwargs={"pk": self.pk})
    



