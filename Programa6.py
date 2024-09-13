lista = [1, 5, 7, 10, 15]
#Suma de la lista
suma = 0
for valor in lista:
    suma += valor
print("La suma de los valores en la lista es:", suma)
print()
#Agregar numeros a la lista
for i in range(3):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)
print()
#Mostrar los numeros de la lista uno por uno 
print("los numeros de la lista son:")
for elemento in lista:
    print(elemento)
#Realizar de nuevo la suma 
suma1 = 0
for valor in lista:
    suma1 += valor
print("La suma de los valores que se suman es:", suma1)
print()
# Imprimir
lista2 = [[1,2,3],[4,5,6],[7,8,9]]
print(lista2)
for elemento2 in lista2:
    print()
    for elemento3 in elemento2:
        print(elemento3, end=' ')
#imprimir con mas pedos
#for elemento2 in range(len(lista2)):
    #for elemento3 in range (len(lista2[elemento2]))
       # print(lista2[x][4], end=' ')
       # print()
#otro
l=[]
for i in range(1,11):
    l.append(i**3)
    print(l)
l=[i**3 for i in range(1,11)]
    print(l)
