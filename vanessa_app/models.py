from django.db import models

class Cliente(models.Model):
    
    nome = models.CharField(max_length=30)
    celular = models.CharField(max_length=13, default="")
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):

        return self.nome

class Servico(models.Model):

    NIVEL = (
        ('Corporal','Corporal'),
        ('Pé e Mão','Pé e Mão'),
        ('Depilação','Depilação'),
        )
    codigo_servico = models.CharField(max_length=30)
    descricao = models.CharField(max_length=9)
    nivel = models.CharField(max_length=30, choices=NIVEL, blank=False, default ='C')

    def __str__(self):
        return self.descricao


class Atendimento(models.Model):

    PRECOS = (
        (30,30),
        (40,40),
        (50,50),
    )
    precos = models.IntegerField(choices=PRECOS, blank=False)
    service = models.ForeignKey(Servico, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    #def __str__(self):
    #return "{}".format(self.client_name)

   
        

   


