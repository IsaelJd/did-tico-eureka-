# ex061 Melhorado porém, resolvido em menos linha.
primeirotermo = int(input('Primero termo: '))
razao = int(input('Razão: '))
termo = primeirotermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} >', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('''Quantos termos a mais você quer mostrar:
> '''))
print('FIM')
print(f'Progressa finalizada com {total} de mostrados')
