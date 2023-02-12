import os

palavra_secreta = 'perfume'
tentativas = ''

while True:
    
    letra = input('Digite uma letra: ')
    
    if letra.isdigit():
        print('Digite uma letra e não um número.')
        continue
    
    if len(letra) > 1:
        print('Digite apenas uma letra por vez.')
        continue
    
    tentativas += letra

    adivinha = ''

    for i in palavra_secreta:
        if i in tentativas:
            adivinha += i
        else:
            adivinha += '*'
    
    print(adivinha)

    if adivinha == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU, PARABÉNS!!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {len(tentativas)}')
        tentativas = ''
        continue