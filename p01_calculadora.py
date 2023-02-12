numero1 = 0
numero2 = 0
operador = ''

while True:

    sair = input('Quer sair? [s]im ')

    if sair.lower() == 's' or sair.lower().startswith('s'):
        break

    numero1_input = input('Digite o primeiro número: ')
    numero2_input = input('Digite o segundo número: ')

    try:
        numero1 = float(numero1_input)
        numero2 = float(numero2_input)
    except:
        print('Valor digitado incorreto, tente novamente')
        continue

    while True:

        operador = input('Digite o operador: \n[+] Adição [-] Subtração \n[*] Multiplicação [/] Divisão: ')
        
        if operador =='+':
            print(f'O resultado da operação é {numero1+numero2}')
        elif operador == '-':
            print(f'O resultado da operação é {numero1 - numero2}')
        elif operador == '*':
            print(f'O resultado da operação é {numero1 * numero2}')
        elif operador == '/':
            print(f'O resultado da operação é {(numero1 / numero2):.2f}')
        else:
            print('Operação inválida, digite novamente')
            continue

        break

