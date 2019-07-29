from django.db import models

# Create your models here.
class Plano(models.Model):
    cd_plano = models.IntegerField(primary_key=True)
    nm_plano = models.CharField(max_length=40)
    menor_percent = models.FloatField()
    maior_percent = models.FloatField()
    valor_minimo = models.FloatField()


class Vendedor(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nm_vendedor = models.CharField(max_length=60)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11)
    idade = models.IntegerField()
    email = models.CharField(max_length=60)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)