perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções':['1','3','4','5'],
        'Resposta':'4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções':['25','55','10','51'],
        'Resposta':'25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções':['4','5','2','1'],
        'Resposta':'5',
    },
]
certas = 0
indice_certo = ''

for i in perguntas:
    print('\nPergunta:',i['Pergunta']+'?','\n\nOpções:')

    for indice,j in enumerate(i['Opções']):
        print(f'{indice}) {j}')
        if i['Resposta'] == j:
            indice_certo = str(indice)

    escolha = input('Escolha uma opção: ')

    if escolha == indice_certo:
        print('Acertou ✅')
        certas += 1
    else:
        print('Errou ❌')

print(f'Você acertou {certas} de {len(perguntas)} perguntas')