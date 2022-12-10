msg = (' Treinando Condições ')
print('{:=^50}'.format(msg))

nome = str(input('\nInforme o seu nome: ')).strip().upper()
if nome == ('ANDRÉ'):
    print('\nOlá {}, que nome lindo você tem!'.format(nome.capitalize()))
else:
    print('\nOlá {}, seu nome é bem comum...'.format(nome.capitalize()))
print('Tenha um ótimo dia!')


