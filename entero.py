print("-------------------------------------------------------------------")
print("----------------------------CENTNELA-------------------------------")
print("-----------------NÚMEROS ENTEROS PARES E IMPARES-------------------")

#Input
n = int(input("Ingrese un número: "))

par = 0
impar = 0  

#PROCESS
while n != 0:
    r = n % 2
    if r == 0:
        par = par + 1 
    else: 
        impar = impar + 1 
    n = int(input("Digite un número "))

#OUTPUT
print("La cantidad de números pares es " ,par, "e impares es " , impar)