print('FATORIAL')


num = int(input('Digite um número para calcular o fatorial: '))

c = num
mult = 0
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else ' = ', end=' ')
    mult = num * c
    
    c -= 1
        
