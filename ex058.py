# Jogo de adivinhação
from random import randint
tentativa = 1
print('Vou pensar em um numero\nTente divinhar.')
computador = randint(1, 10)
player = int(input('De o seu palpite: '))

while computador != player:
    if computador > player:
        print('Mais')
    elif computador < player:
        print('Menos')
    tentativa += 1
    player = int(input('Tente novamente:'))
if tentativa == 1:
    print(f'O numero escolhido foi {computador}\n'
          f'Ganhou essa.')
elif tentativa == 2:
    print('De sengunda em.')
elif tentativa > 2:
    print('Finalmente. Achei que não acertaria mais kkkkkk.')
print(f'Você precisou de {tentativa} tentativa.')
