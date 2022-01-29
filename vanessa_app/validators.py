import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome_cliente):
    return nome_cliente.isalpha()

def celular_valido(numero_celular):
    #Formato de celular válido: (11 96464-4244)
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    verifica_se_formato_valido = re.findall(modelo, numero_celular)
    return verifica_se_formato_valido
        
