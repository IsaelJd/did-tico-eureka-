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
        if escolha == 1:
            print('Soma')
            print(f'{numero1} + {numero2} = {numero1 + numero2}')
            print('-'*30)
            continuar = str(input('Outra duvida? [S/N] ')).strip().upper()[0]
            print('-'*30)
        elif escolha == 2:
            print('Multiplicação')
            print(f'{numero1} x {numero2} = {numero1 * numero2}')
            print('-'*30)
            continuar = str(input('Outra duvida? [S/N] ')).strip().upper()[0]
            print('-'*30)
        elif escolha == 3:
            print('Saber qual é maior.')
            if numero1 > numero2:
                print(f'O numero {numero1} é o maior')
                print('-'*30)
                continuar = str(
                    input('Outra duvida? [S/N] ')).strip().upper()[0]
                print('-'*30)
            else:
                print(f'O numero {numero2} é o maior')
                print('-'*30)
                continuar = str(
                    input('Outra duvida? [S/N] ')).strip().upper()[0]
                print('-'*30)
        elif escolha == 4:
            print('Novos Valores')
            print('Digite os Novos valores.')
            print('-'*30)
        elif escolha == 5:
            continuar = 'N'
print('FIM')
