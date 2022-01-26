from django.http import JsonResponse
from rest_framework import viewsets, generics
from vanessa_app.models import Cliente, Servico, Atendimento
from vanessa_app.serializer import ClienteSerializer, ServicoSerializer, AtendimentoSerializer,ListaServicosPorCliente, ClienteSerializerV2
from rest_framework.response import Response


class ClientesViewSet(viewsets.ModelViewSet):
    ##Exibindo todos os clientes
    queryset = Cliente.objects.all()
  
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ClienteSerializerV2
        else:
            return ClienteSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    ##Exibindo todos os serviços
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    def create(self, request): #def responável por criar um location no console do navegador onde ficará salvo o endpoint da criação do serviço 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data(['id']))
            response['Location'] = request.build_absolute_uri() + id
            return response

class AtendimentoViewSet(viewsets.ModelViewSet):
    ##Exibindo todos os atendimentos
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer
    http_method_names = ['get','post', 'put', 'path', 'delete'] # aqui eu acrescento os verbos que eu quiser 

class ListaAtendimentoCliente(generics.ListAPIView):
    ##listando atendimentos por cliente ID
    def get_queryset(self):
        queryset = Atendimento.objects.filter(client_name_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaServicosPorCliente



    


