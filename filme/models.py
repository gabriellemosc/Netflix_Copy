from django.db import models
from django.utils import timezone  #para pegar a hora que salvar a data de criação
# Create your models here.

#filmes
LISTA_CATEGORIAS = (  
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS","Outros")

)

class Filme(models.Model):  #subclasse do model
    titulo = models.CharField(max_length=100)                               #definir quantos valores char terá o titúlo. 1 linha apenas de campo
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=10000)                          #escrever texto
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS )  #passamos a lista criada fora da classe
    visualizacoes = models.IntegerField(default=0)                           #valor padrão 0
    data_criacao = models.DateTimeField(default=timezone.now)                #pegar o valor que foi criado o filme

    def __str__(self):
        return self.titulo