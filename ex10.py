def positivos(numeros):
    lista=[x for x in numeros if x >0]
    return lista


nums=[5,3,45,-2,1,-8,0]
print(positivos(nums))