numero ='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
num = 0
while True:
    num = int(input('Digite um número: '))
    if num >= 0 and num <= 20:  
        for extenso in range(0, len(numero)):
            if num == extenso:
                print(numero[extenso])
    else: 
        print('Digite novamente')

 


#TESTE