nome = str(input('Digite seu nome: ')).strip().title()
print(f'Olá, {nome}!')
if nome == 'Caio' or 'Monica' or 'Pedro' or 'Isael':
    print('Que lindo nome você tem.')
elif nome == 'Joana' or 'Kaline' or 'Kailanne':
    print('Que nome diferente')
else:
    print('Nome normal.')
