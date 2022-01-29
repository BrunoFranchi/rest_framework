from rest_framework import serializers
from vanessa_app.models import Servico, Cliente, Atendimento
from vanessa_app.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate(self, data): # Na def criada no arquivo validators teremos um retono True or False 
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF Inválido'})

        if not nome_valido(data['nome']): # Na def criado no arquivo validators teremos um retono True or False 
            raise serializers.ValidationError({'nome':'Nome Inválido'})


class ClienteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome','celular','rg','cpf','data_nascimento']
        
    def validate(self, data): # Na def criada no arquivo validators teremos um retono True or False
        if not celular_valido(data['celular']): # Checando se o numero do celular foi preenchido no formato aceito
            raise serializers.ValidationError({'celular':'Celular preenchido no formato inválido'})
        return data

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class AtendimentoSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField(source='get_client_name')
    service = serializers.SerializerMethodField(source='get_service')
    
    class Meta:
        model = Atendimento
        fields = '__all__'
    
    def get_client_name(self, obj):
        return obj.client_name.nome
    
    def get_service(self, obj):
        return obj.service.nivel

class ListaServicosPorCliente(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client_name.nome')
    service = serializers.ReadOnlyField(source='service.descricao')
    class Meta:
        model = Atendimento
        exclude = []
