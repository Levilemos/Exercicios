def tamanhos(palavras):
    lista=[len(p) for p in palavras]
    return lista

nomes=["python", "java", "javascript", "c"]
print(tamanhos(nomes))