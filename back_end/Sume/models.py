from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class NaturezasDespesa(models.Model):
    id_natureza_despesa = models.AutoField(primary_key = True)
    cod_natureza_despesa = models.CharField(max_length=8)
    desc_natureza_despesa = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.desc_natureza_despesa

class Projetos(models.Model):
    id_projeto = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 100)
    dt_inicio_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField()
    id_user_cad = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'user_cad')
    dt_cad = models.DateField(auto_now_add = True)
    id_user_alt = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'user_alt', null = True)
    dt_alt = models.DateField(null = True, blank= True, auto_now = True)

    def __str__(self) -> str:
        return self.titulo

class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key= True)
    razao_social = models.CharField(max_length= 100)
    cnpj = models.CharField(max_length= 20, unique= True)
    email = models.EmailField(max_length= 50)
    telefone = models.CharField(max_length= 20)
    id_user_cad = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add = True)
    id_user_alt = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_alt', null = True)
    dt_alt = models.DateField(null = True, blank= True, auto_now = True)

    def __str__(self) -> str:
        return self.razao_social

class Ordens (models.Model):
    id_ordem = models.AutoField(primary_key= True)
    id_projeto = models.ForeignKey(Projetos, on_delete=models.Case) 
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.Case)
    id_natureza_despesa = models.ForeignKey(NaturezasDespesa, on_delete=models.Case)
    numero = models.IntegerField()
    ano = models.IntegerField()
    id_user_cad = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add = True)
    id_user_alt = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_alt', null = True)
    dt_alt = models.DateField(null = True, blank= True, auto_now = True)

    def __str__(self) -> str:
        return str(self.id_projeto) +'/' +str(self.id_fornecedor)

class ItensOrdens (models.Model):
    id_item_ordem = models.AutoField(primary_key= True)
    id_ordem = models.ForeignKey(Ordens, on_delete= models.Case)
    produto_servico = models.CharField(max_length= 100)
    qtd = models.IntegerField()
    valor_unitario = models.IntegerField()
    id_user_cad = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add = True)
    id_user_alt = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_alt', null = True)
    dt_alt = models.DateField(null = True, blank= True, auto_now = True)

    def __str__(self) -> str:
        return self.produto_servico

class Contratos (models.Model):
    id_contrato = models.AutoField(primary_key= True)
    id_prestador = models.IntegerField()
    numero = models.IntegerField()
    ano = models.IntegerField()
    data_inicio_vigencia = models.DateField()
    data_fim_vigencia = models.DateField()
    objeto = models.CharField(max_length= 25)
    id_user_cad = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add = True)
    id_user_alt = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_alt', null = True)
    dt_alt = models.DateField(null = True, blank= True, auto_now = True)

    def __str__(self) -> str:
        return self.objeto

class ItensContrato (models.Model):
    id_item_contrato = models.AutoField(primary_key= True)
    id_contrato = models.ForeignKey(Contratos, on_delete= models.Case)
    id_item_ordem = models.ForeignKey(ItensOrdens, on_delete= models.Case)
    qtd = models.IntegerField()
    valor_unitario = models.IntegerField()
    id_user_cad = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add = True)
    id_user_alt = models.ForeignKey(User, on_delete= models.CASCADE, related_name= '%(class)s_user_alt', null = True)
    dt_alt = models.DateField(null = True, blank= True, auto_now = True)


    def __str__(self) -> str:
        return str(self.id_contrato) +'/' +str(self.id_item_ordem)

class Vigencias (models.Model):
    id_vigencia = models.AutoField(primary_key= True)
    id_contrato = models.ForeignKey(Contratos, on_delete= models.Case)
    dt_inicio_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField()
    valor = models.IntegerField()

    def __str__(self) -> str:
        return self.id_vigencia
        