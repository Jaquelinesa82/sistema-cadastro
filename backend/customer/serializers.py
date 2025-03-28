from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    peso_ideal = serializers.SerializerMethodField()
    
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'data_nasc', 'cpf', 'sexo', 'altura', 'peso', 'peso_ideal']
        
    def get_peso_ideal(self, obj):
        return obj.calcular_peso_ideal()