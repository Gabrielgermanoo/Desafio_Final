from rest_framework import serializers

from . import models

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projetos
        fields = '__all__'
        
