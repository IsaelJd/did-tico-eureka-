# Validando sexo da pessoa com While
sexo = str(
    input('Qual o seu sexo\n[F] Feminino\n[M] Masculino\n> ')).strip().upper()
while sexo != 'F' and sexo != 'M':
    print(f'A resposta {sexo} é invalida\nTente novamente')
    sexo = str(
        input('Qual o seu sexo\n[F] Feminino\n[M] Masculino\n> ')).strip().upper()
if sexo == 'F':
    print('Seu sexo é Feminino.')
elif sexo == 'M':
    print('Seu sexo é Masculino')
