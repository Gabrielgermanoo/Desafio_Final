from rest_framework import serializers

from . import models

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projetos
        fields = '__all__'
        
class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedores
        fields = '__all__' # ['id_projeto',"titulo"]

class NaturezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NaturezasDespesa
        fields = '__all__' # ['id_projeto',"titulo"]

class OrdensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ordens
        fields = '__all__' # ['id_projeto',"titulo"]

class ItemOrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensOrdem
        fields = '__all__' # ['id_projeto',"titulo"]

class ContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contratos
        fields = '__all__' # ['id_projeto',"titulo"]

class VigenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vigencias
        fields = '__all__' # ['id_projeto',"titulo"]

class ItemContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensContratos
        fields = '__all__' # ['id_projeto',"titulo"]