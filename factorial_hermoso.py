""""
Una permutación de los enteros 1, 2, ..., n se denomina “buena” si no hay elementos
adyacentes cuya diferencia sea 1.
"""

def factorial_hermoso(n):
    if n<=3:
        return "No hay sol"
    lista_per=[]
    lista_sol=[]
    lista_pares=[]
    lista_impares=[]

    for i in range(n,0,-1):
        lista_per.append(i)
    
    for i in range(len(lista_per)):
        if lista_per[i]%2==0:
            lista_pares.append(lista_per[i])
        else:
            lista_impares.append(lista_per[i])

    lista_sol=lista_impares+lista_pares
    return lista_sol

print(factorial_hermoso(5))
print(factorial_hermoso(3))