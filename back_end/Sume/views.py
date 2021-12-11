from django.shortcuts import render
from . import serializers
from rest_framework import viewsets
from . import models

class ProjetoView(viewsets.ModelViewSet):
    queryset = models.Projetos.objects.all()
    serializers_class = serializers.ProjetoSerializer
