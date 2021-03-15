# ex061 melhorado com opção de ver mais termos
from time import sleep
primeirotermo = int(input('Primero termo: '))
razao = int(input('Razão: '))
termo = primeirotermo
cont = 1
while cont <= 10:
    print(f'{termo}', end='')
    print('> ', end='')
    termo += razao
    cont += 1
print('PAUSA')
print('=-='*15)
mais = 1
totaltermos = cont
while mais != 0:
    mais = int(input('''
Quer ver mais termos dessa PA?
Quantos
>'''))
    maistermos = cont
    while maistermos < (mais + cont):
        print(f'{termo}', end='')
        print('> ', end='')
        termo += razao
        maistermos += 1
        totaltermos += 1
print('Finalizando....')
sleep(.5)
print('Você solicitou ', end='')
print(f'{cont -1}' if cont == totaltermos else f'{totaltermos -1}', end='')
print(' termos dessa PA')
