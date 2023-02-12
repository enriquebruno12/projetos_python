import os

lista = []

while True:
    escolha = input('Selecione uma opção: \n[i]nserir [a]pagar [l]listar: ').lower()

    if escolha == 'i':
        os.system('cls')
        produto = input('Digite o produto: ')
        lista.append(produto)
        os.system('cls')
        print('Produto inserido com sucesso')

    elif escolha == 'a':
        os.system('cls')
        
        if lista == []:
            print('Não há nada para apagar.')
            continue

        for i,j in enumerate(lista):
            print(i,j)
        
        while True:
            indice = input('Digite o índice que deseja apagar: ')
            
            try:
                lista.pop(int(indice))
                print('Item deletado com sucesso!')
                break
            except ValueError:
                print('Digite um valor numérico')
                continue
            except IndexError:
                print('Digite um valor de índice que exista na lista')
                continue
            except:
                print('Erro desconhecido')
                continue
    elif escolha == 'l':

        os.system('cls')

        if lista == []:
            print('Não há nada para listar.')
            continue
        
        for a,b in enumerate(lista):
            print(a,b)
    
    else:
        os.system('cls')
        print('Você digitou um valor inválido, por favor, tente novamente.')
        continue