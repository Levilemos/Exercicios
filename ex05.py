def filtrar(lista):
    maiores=[nome for nome in lista if len(nome)>5]
    return maiores

nomes=["Levi","João","Alberto","Luiz","Jennifer"]
print(filtrar(nomes))