from django.db import models
from django.utils import timezone


        
        
class Type(models.Model):
    acronimos = models.CharField(max_length=5)
    descricao = models.TextField()
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.acronimos

    
class Tags(models.Model):
    acronimos = models.CharField(max_length=5)
    descricao = models.TextField()
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.acronimos


class Apresentadores(models.Model):
    nome = models.CharField(max_length=10)
    filiacao = models.CharField(max_length=20)
    resume = models.TextField()
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.nome
    
class Sala(models.Model):
    nome = models.CharField(max_length=10)
    capacidade = models.IntegerField
    local = models.TextField()
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.nome
   

class Atividade(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    tipo = models.ForeignKey('Type')
    tags = models.ForeignKey('Tags')
    sala = models.ForeignKey('Sala')
    data_hora_inicio = models.DateTimeField(
            default=timezone.now)
    data_hora_fim = models.DateTimeField(
            default=timezone.now)
    apresentadores = models.ForeignKey('Apresentadores')
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.title

