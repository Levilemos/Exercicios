def primo(n):
    if n < 2:
        return False

    divisores = 0

    for c in range(1, n + 1):
        if n % c == 0:
            divisores += 1

    return divisores == 2

n = int(input())

lista = [x for x in range(1, n + 1) if primo(x)]

print(lista)