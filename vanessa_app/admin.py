from django.contrib import admin

from vanessa_app.models import Cliente, Servico, Atendimento

class Clientes(admin.ModelAdmin):
    
    list_display = ('id','nome','rg','cpf','data_nascimento')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)

class Servicos(admin.ModelAdmin):
    list_display = ('id','codigo_servico','descricao',)
    search_fields = ('codigo_servico',)

admin.site.register(Servico, Servicos)

class Atendimentos(admin.ModelAdmin):
    list_display = ('client_name','service','precos' )
  
admin.site.register(Atendimento, Atendimentos)

