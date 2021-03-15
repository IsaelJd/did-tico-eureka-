# Verificando sexo e idade. Depois categorizando.
total = 0
totalmulher = 0
mulheres = 0
# validação de presença masculinha na lista
velho = 0
homemvelho = ''
confirmacao = 0
for c in range(1, 5):
    nome = str(input(f'Nome da {c}ª pessoa: ')).strip().title()
    idade = int(input(f'Idade da {c}ª pessoa: '))
    sexo = str(input(f'Sexo da {c}ª pessoa:\n'
                     f'[F] Feminino\n'
                     f'[M] Masculino\n'
                     f'> ')).strip().capitalize()
    total += idade
    if sexo == 'F':
        totalmulher += 1
        if idade >= 20:
            mulheres += 1
    if sexo == 'M':
        confirmacao += 1
        if idade > velho:
            velho = idade
            homemvelho = nome

media = total / 4
print('A media de idade é de {:.0f}'.format(media))
# variação da resposta para mulheres maiores de 20
if mulheres < 2:
    print(f'Das {totalmulher} mulheres da lista apenas '
          f'{mulheres} é maiores de 20 anos')
elif mulheres < totalmulher:
    print(f'Das {totalmulher} mulheres da listadas apenas '
          f'{mulheres} são maiores de 20 anos')

elif totalmulher == mulheres:
    print(f'Todas as {totalmulher} mulheres da lista são maiores de 20 anos')

# variação da resposta para o homem mais velho
if confirmacao >= 1:
    print(f'E o Sr.{homemvelho} é o homem mais velho, com seus {velho} anos.')
else:
    print('Não a nenhum homem na lista')
