# Generated by Django 4.0 on 2021-12-10 19:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Sume', '0002_fornecedores_projetos_ordens'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensOrdens',
            fields=[
                ('id_item_ordem', models.AutoField(primary_key=True, serialize=False)),
                ('produto_servico', models.CharField(max_length=100)),
                ('qtd', models.IntegerField()),
                ('valor_unitario', models.IntegerField()),
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_ordem', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='Sume.ordens')),
                ('id_user_alt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_user_alt', to='auth.user')),
                ('id_user_cad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_user_cad', to='auth.user')),
            ],
        ),
    ]
