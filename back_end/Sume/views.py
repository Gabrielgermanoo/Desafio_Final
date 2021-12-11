from django.shortcuts import render
from . import serializers
from rest_framework import viewsets
from . import models
from rest_framework.response import Response

class ProjetoView(viewsets.ModelViewSet):
    queryset = models.Projetos.objects.all()
    serializers_class = serializers.ProjetoSerializer
class ContratosView(viewsets.ModelViewSet):
    queryset = models.Contratos.objects.all()
    serializer_class = serializers.ContratosSerializer

class FornecedoresView(viewsets.ModelViewSet):
    queryset = models.Fornecedores.objects.all()
    serializer_class = serializers.FornecedorSerializer


# metodo get

    def list(self, request):
        contratos = models.Contratos.objects.all()

        itensordem = models.ItensOrdem.objects.all()
        
        lista_contratos = []

        lista_itens_ordem = []

        #Contratos

        for contrato in contratos:
            vigencias = models.Vigencias.objects.filter(id_contrato=contrato)
            itenscontrato = models.ItensContratos.objects.filter(id_contrato=contrato)

            contrato_serializer = serializers.ContratosSerializer(contrato).data
            contrato_serializer['vigencias'] = serializers.VigenciaSerializer(vigencias, many=True).data

            contrato_serializer['itens contratos'] = serializers.ItemContratoSerializer(itenscontrato, many=True).data

            lista_contratos.append(contrato_serializer)        

        
        # Itens Ordem
        for item_ordem in itensordem:

            itenscontrato = models.ItensContratos.objects.filter(id_item_ordem = item_ordem)

            item_ordem_serializer = serializers.ItemOrdemSerializer(item_ordem).data
            item_ordem_serializer['Itens contratos'] = serializers.ItemOrdemSerializer(itenscontrato, many = True).data

            lista_itens_ordem.append(item_ordem_serializer)


        return Response(lista_contratos, lista_itens_ordem)

    def create(self, request):
        prestador = models.Fornecedores.objects.get(id_fornecedor=request.data['id_prestador'])

        contrato = {
            'id_prestador': prestador,
            'numero': request.data['numero'],
            'ano': request.data['ano'],
            'objeto': request.data['objeto']
        }

        contrato_obj = models.Contratos.objects.create(**contrato)

        vigencia = {
            'id_contrato': contrato_obj,
            'dt_inicio_vigencia': request.data['data_inicio_vigencia'],
            'dt_fim_vigencia': request.data['data_fim_vigencia']
        }

        models.Vigencias.objects.create(**vigencia)

        return Response({'message':'Contrato e vigencia criados'}, status=500)
