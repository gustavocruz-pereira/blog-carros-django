from django.contrib import admin
from comments.models import Comentario

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('nome_comentario', 'post_comentario', 'publicado_coment')
    list_editable = ('publicado_coment',)



admin.site.register(Comentario, CommentsAdmin)
