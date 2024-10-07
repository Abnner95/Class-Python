num = int(input('Digite um número: '))
soma = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        soma += 1
    else:
        print('\033[34m', end=' ')
    print(f'{c}', end=' ')
if soma >2:
    print(f'\n\033[m O número {num} não é primo, pois ele foi divisivel {soma} vezes')
else:
    print(f'\n\033[m O número {num} é primo, pois ele foi divisivel {soma} vezes')
    #if num % 2 !=0 and num :
    #   print(num)
