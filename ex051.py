print('PROGRESSÃO ARITIMÉTICA')
primeiro = int(input('Digite um número: ')) 
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(primeiro, end=' ->')
    primeiro += razao  
print('FIM')
    
