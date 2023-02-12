import re
import sys

entrada = input('[CPF]: ')
entrada_form = re.sub(r'[^0-9]','',entrada)

primeiro_char =  entrada == entrada[0] * len(entrada)

if primeiro_char:
     print('Você enviou dados sequenciais')
     sys.exit()

cpf_9 = entrada_form[:9]
i = 10
soma = 0 

for valor in cpf_9:
     soma += int(valor) * i
     i -= 1

calculo = (soma * 10) % 11

digito1 = 0 if calculo > 9 else calculo

i = 11
soma = 0
cpf_10 = cpf_9 + str(digito1)

for valor in cpf_10:
     soma += int(valor) * i
     i -= 1

calculo = (soma * 10) % 11

digito2 = 0 if calculo > 9 else calculo

cpf_validado = f'{cpf_9}{digito1}{digito2}'

if cpf_validado == entrada_form:
    print(f'CPF: {entrada_form} é válido')
else:
    print(f'CPF: {entrada_form} é inválido')