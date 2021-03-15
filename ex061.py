# Descubra os 10 primeros termos de uma PA
primeirotermo = int(input('Primero termo: '))
razao = int(input('Razão: '))
termo = primeirotermo
cont = 1
while cont <= 10:
    print(f'{termo} >', end='')
    termo += razao
    cont += 1
print('FIM')
