from django.contrib import admin
from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','author', 'published')
    list_editable = ('published',)
    summernote_fields = ('content')

admin.site.register(Post, PostAdmin)
