media = 0
somaIdade = 0
Maioridade = 0
NomeMaior =''
totmulher =0
for c in range(1,5):
    print(5*'-',f'{c}ª pessoa',5*'-')
    nome = str(input('Nome: '))
    idade = int(input('idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    somaIdade += idade
    if c==1 and sexo == 'M':
        Maioridade = idade
        NomeMaior = nome
    if sexo == 'M' and idade > Maioridade:
        Maioridade = idade
        NomeMaior = nome
    if sexo == 'F' and idade < 20:
        totmulher += 1

media = somaIdade / c
print(f'A média do grupo é {media} anos')
print(f'O homem mais velho do grupo é {NomeMaior} com {Maioridade} anos de idade')
print(f'Tem {totmulher} menor de 20 anos de idade ')