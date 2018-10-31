from django.db import models


class Setor(models.Model):
    '''Modelo de dados para setores da empresa'''
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    '''Modelo de dados para os funcionários da empresa'''
    nome = models.CharField(max_length=255)
    setor = models.ForeignKey(Setor, null=True, 
                              on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome
