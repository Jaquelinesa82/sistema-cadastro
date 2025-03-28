from django.db import models
from decimal import Decimal


class Pessoa(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    data_nasc = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name='CPF')
    sexo = models.CharField(max_length=1, choices=[('m', 'Masculino'), ('f', 'Feminino')])
    altura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Altura')
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso')
    
    def calcular_peso_ideal(self):
        altura = Decimal(self.altura)  # Garantir que altura seja Decimal
        if self.sexo == 'm':
            return (Decimal('72.7') * altura) - Decimal('58')
        else:
            return (Decimal('62.1') * altura) - Decimal('44.7')

    
    def __str__(self):
        return self.nome
