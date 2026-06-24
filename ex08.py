def pares(inteiros):
    lista=[x for x in inteiros if x % 2 ==0]
    return lista

inteiros=[1,2,3,4,5,6,7,8,9,10]
print(pares(inteiros))