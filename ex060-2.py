# Descubra o fatorial com um numero (Com WHILE e Detalhado)
numero = int(input('Digite um número: '))
c = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(f'{fatorial}')
