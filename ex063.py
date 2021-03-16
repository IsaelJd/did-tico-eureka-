# Digite um numero e veja a sequencia Fibonacci
n = int(input('Digite quantos elementos da Sequencia você deseja ver: '))
cont = 0
f1 = 0
f2 = 1
print(f'{f1} + {f2} + ', end='')
cont = 3
while cont <= n:
    f3 = f1 + f2
    cont += 1
    print(f'{f3}', end='')
    print(' + ' if cont <= n else '', end='')
    f1 = f2
    f2 = f3
print('...')
