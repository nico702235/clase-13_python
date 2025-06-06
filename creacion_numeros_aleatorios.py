import random #libreria para llamar y crear numeros random

numero = []

for i in range(100): #ciclo para repetir 10 veces las iteraciones 
    n = random.randint(1,100) #crea un numero entre 1 y el 100
    numero.append(n) #Guardamos en la lista el numero

print(numero) #visualizamos lista

cont= 0

for i in range (len(numero)):
    if numero[i]%2==0:
        cont+=1

print(f"cantidad de numeros pares : {cont}")
