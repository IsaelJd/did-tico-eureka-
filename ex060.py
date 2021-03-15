# Descubra o Fatorial de um numero (Com WHILE)
numero = int(input('Digite um valor: '))
fatorial = 1
contador = 1
while contador <= numero:
    fatorial = fatorial * contador
    contador += 1
print(f'O fatorial de {numero} é {fatorial}')
