def achatar(lista):
    resultado = []
    for x in lista:
        if isinstance(x, list):
            resultado += achatar(x)
        else:
            resultado.append(x)
    return resultado

#com compreensão
def achatar_comp(lista):
    return [x for x in lista if not isinstance(x, list)] + \
           [x for sublista in lista if isinstance(sublista, list) for x in achatar_comp(sublista)]

lst = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]

print(achatar(lst))       
print(achatar_comp(lst))  