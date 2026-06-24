def vogais(string):
    qtd=[1 for vogal in string if vogal in "aeiou"]
    return len(qtd)
nome=input()
print(vogais(nome))