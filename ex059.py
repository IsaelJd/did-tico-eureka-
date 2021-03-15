# Calculadora com MENU
from time import sleep
sair = ''
while not sair == 'ok':
    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite outro numero: '))
    escolha = 0
    while not escolha == 4:
        escolha = int(input('''Escolha uma opção
[1] Soma
[2] Multiplicar
[3] Maior Valor
[4] Novo numero
[5] Sair
> '''))
        if escolha == 1:
            print('Soma')
            print(f'{numero1} + {numero2} = {numero1 + numero2}')
            print('=-='*30)
        elif escolha == 2:
            print('Multiplicar')
            print(f'{numero1} x {numero2} = {numero1 * numero2}')
            print('=-='*30)
        elif escolha == 3:
            if numero1 > numero2:
                print(f'O numero {numero1} é maior que o numero {numero2}')
                print('=-='*30)
            else:
                print(f'O numero {numero2} é maior que o numero {numero1}')
                print('=-='*30)
        elif escolha == 4:
            print('=-='*30)
        elif escolha == 5:
            escolha = 4
            sair = 'ok'
        else:
            print('Opção INVÁLIDA')
print('Finalizando ....')
sleep(1.5)
print('FIM')
