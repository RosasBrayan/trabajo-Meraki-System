def CreacionDeNumeros(inicio,fin,restriccion1,restriccion2):
    for i in range (inicio,fin+1):
        if (i != restriccion1) and ( i%3 != 0):
            lista1.append(i)
            
def fibonacci(n):
    if(n==0) or (n==1):
        return(n)
    else:
        return (fibonacci(n-2)+fibonacci(n-1))
    
def listaFibo(n):
    for i in range (0,n,):
        listaFibonacci.append(fibonacci(i))
        
def comparador(x):
    for i in listaFibonacci:
        if x==i :
            return True
    return False

#Brayan Rosas Ayala
lista1 = []
lista2 = []
listaFibonacci = []
matriz =[]

CreacionDeNumeros(10,55,16,3)
matriz.append(lista1)
print("la lista es :\n", lista1)

listaFibo(11)
print("\nla lista fibonnacci :\n", listaFibonacci)

for x in lista1:
    lista2.append(comparador(x))
matriz.append(lista2)
print("\nla matriz es :\n", matriz)


print("\nnumero  ¿Cumple la sucesion?")
for i in range(0,len(lista1)):
    print(matriz[0][i], "      ", matriz[1][i])
