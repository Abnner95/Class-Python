sexo =str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo =str(input('Dados invalidos. Digite os dados novamente: ')).strip().upper()[0]
if sexo == 'F':
    print(f'Muito bem senhora, seu registro de sexo {sexo} foi cadastrado com sucesso ')
else:
    print(f'Muito bem senhor, seu registro de seox {sexo} foi cadastrado com sucesso ')
