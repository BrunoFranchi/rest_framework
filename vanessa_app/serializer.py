from rest_framework import serializers
from vanessa_app.models import Servico, Cliente, Atendimento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome','rg','cpf','data_nascimento']

class ClienteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome','celular','rg','cpf','data_nascimento']

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
