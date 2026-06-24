def descendentes(arvore):
    nome, filhos = arvore
    return [
        descendente
        for filho in filhos
        for descendente in [filho[0]] + descendentes(filho)
    ]


arvore = (
    "Ana",
    [
        (
            "Bruno",
            [
                ("Carlos", []),
                ("Daniel", [])
            ]
        ),
        (
            "Eva",
            [
                ("Felipe", [])
            ]
        )
    ]
)

print(descendentes(arvore))