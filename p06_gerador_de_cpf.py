import random

cpf_9 = ''

for i in range(9):
    cpf_9 += str(random.randint(0,9))

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

print(f'CPF gerado: {cpf_validado}')