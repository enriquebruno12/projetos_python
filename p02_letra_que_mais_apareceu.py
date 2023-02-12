frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por guido van Rossum'

i = 0
mais_apareceu = ''
qtd_maior = 0

while i < len(frase):
    
    if frase[i] != ' ':
        qtd_atual = frase.count(frase[i])
    

    if qtd_atual > qtd_maior:
        qtd_maior = qtd_atual
        mais_apareceu = frase[i]
    i += 1

print(f'Quem mais apareceu foi o "{mais_apareceu}", aparecendo um total de {qtd_maior} vezes')