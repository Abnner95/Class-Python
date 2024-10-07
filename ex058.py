num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opção = 0
result = 0
while opção !=5 :
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        result = num1 + num2
        print(f'A soma dos números é = {result}')
    elif opção ==2:
        result = num1 * num2
        print(f'A multiplicação dos números é = {result}')
    elif opção ==3:
        if num1 > num2:
            result = num1
        else: result = num2
        print(f'O maior número digitado é  = {result}')
    elif opção ==4:
        num1 = int(input('Digite o primeiro numero:  '))
        num2 = int(input('Digite o segundo número: '))
    elif opção ==5:
        print('Você optou por sair, até mais ')
        break
    else:
        print('Opção invalida, digite novamente!')