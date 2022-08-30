from distutils.command.upload import upload
from django.db import models



class Produtos(models.Model):
    nome_produto = models.CharField(max_length=150, verbose_name='Produto')
    descr_produto = models.CharField(max_length=150, blank=True)
    preco_produto = models.FloatField()
    imagem_produto = models.ImageField(upload_to="media/uploads/%Y/%m/%d")


    def __str__(self) -> str:
        return self.nome_produto
