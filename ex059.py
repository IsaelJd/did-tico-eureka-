prosseguir = ''
continuar = ''
while not continuar == 'N':
    escolha = 0
    while not continuar == 'N':
        numero1 = float(input('Digite um numero: '))
        numero2 = float(input('Digite o outro numero: '))
        escolha = int(input('''Escolha uma opção
    [1] Somar
    [2] Multiplicar
    [3] Saber o maior
    [4] Novos Valores
    [5] Sair
    > '''))
# Escolha 1 (Somando as os 2 input)
        if escolha == 1:
            print('Soma')
            print(f'{numero1} + {numero2} = {numero1 + numero2}')
            print('-'*30)
            continuar = str(input('Outra duvida? [S/N] ')).strip().upper()[0]
            while not prosseguir == 'ok':
                if continuar != 'S' and continuar != 'N':
                    print('Opção INVÁLIDA')
                    continuar = str(input('> ')).strip().upper()[0]
                else:
                    prosseguir = 'ok'
            print('-'*30)
# Escolha 3 (Multiplicando os 2 input)
        elif escolha == 2:
            print('Multiplicação')
            print(f'{numero1} x {numero2} = {numero1 * numero2}')
            print('-'*30)
            continuar = str(input('Outra duvida? [S/N] ')).strip().upper()[0]
            while not prosseguir == 'ok':
                if continuar != 'S' and continuar != 'N':
                    print('Opção INVÁLIDA')
                    continuar = str(input('> ')).strip().upper()[0]
                else:
                    prosseguir = 'ok'
            print('-'*30)
# Escolha 3 (Analisando os 2 input e retornado o maior valor)
        elif escolha == 3:
            print('Saber qual é maior.')
            if numero1 > numero2:
                print(f'O numero {numero1} é o maior')
                print('-'*30)
            elif numero1 < numero2:
                print(f'O numero {numero2} é o maior')
                print('-'*30)
            else:
                print('Não tem numero maior')
                print('-'*30)
            continuar = str(input('Outra duvida? [S/N] ')).strip().upper()[0]
            while not prosseguir == 'ok':
                if continuar != 'S' and continuar != 'N':
                    print('Opção INVÁLIDA')
                    continuar = str(input('> ')).strip().upper()[0]
                else:
                    prosseguir = 'ok'
                print('-'*30)
# Escolhas 4 (Alterar os valores digitados)
        elif escolha == 4:
            print('Novos Valores')
            print('Digite os Novos valores.')
            print('-'*30)
# Escolha 5 (Finalisando o progama)
        elif escolha == 5:
            continuar = 'N'
# Escolha não listada
        else:
            print('Opção INVÁLIDA.')
            continuar = 'S'
print('FIM')
