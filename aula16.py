aula = 'python', 'ingles', 'Desenvolvimento de Sistemas', 'QA'
#print(len(aula))
print(aula)
print(sorted(aula))

print(50*'=')

for  curso in range (0,len(aula)): #aqui vai enumerar a posição da tupla / campo 
    print(aula[curso]) #Quando eu fiz aula[curso] ele escreveu a tupla na posição em que ela esta 

print(50*'=')

for curso in range (0, len(aula)):
    print(curso) #nesse caso ele só trouxe o número em que esta cada tupla / campo 

print(50*'=')
for curso in range(0, len(aula)):
    print(f'Eu estudo {aula[curso]} na ordem {curso}')


