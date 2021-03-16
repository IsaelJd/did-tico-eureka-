from time import sleep
print('Sequencia de Fibonacci')
print('~'*30)
n = int(input('Digite quantos elementos da Sequencia você deseja ver: '))
cont = 0
f1 = 0
f2 = 1
print(f'{f1} - {f2} - ', end='')
cont = 3
mais = n
n2 = 0
while mais != 0:
    n2 = mais + n2
    while cont <= n2:
        f3 = f1 + f2
        cont += 1
        print(f'{f3}', end='')
        print(' - ' if cont <= n2 else '...', end='')
        f1 = f2
        f2 = f3
    print('''
Ver mais elementos ? Digite 0 caso queira finalizar.''')
    mais = int(input('> '))
print('Finalizando...')
sleep(.5)
print('~'*30)
print('Até breve')
