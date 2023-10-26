from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    silga_estado = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=350)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.nome