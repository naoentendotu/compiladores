# ------------------------------------------------
#     Analisador Sintático Preditivo LL(1)
#     Gramática: Declarações de variáveis
# ------------------------------------------------

tabela = {
    ("S", "int"): ["D", "S"],
    ("S", "float"): ["D", "S"],
    ("S", "char"): ["D", "S"],
    ("S", "$"): ["ε"],

    ("D", "int"): ["T", "L", ";"],
    ("D", "float"): ["T", "L", ";"],
    ("D", "char"): ["T", "L", ";"],

    ("T", "int"): ["int"],
    ("T", "float"): ["float"],
    ("T", "char"): ["char"],

    ("L", "id"): ["id", "L′"],

    ("L′", ","): [",", "id", "L′"],
    ("L′", ";"): ["ε"]
}

def analisador(tokens):
    tokens = tokens + ["$"]
    pilha = ["$", "S"]

    while pilha:
        topo = pilha.pop()
        lookahead = tokens[0]

        if topo == "ε":
            continue

        if topo in ["int", "float", "char", "id", ",", ";", "$"]:
            if topo == lookahead:
                tokens.pop(0)
            else:
                return False
        else:
            chave = (topo, lookahead)
            if chave in tabela:
                producao = tabela[chave]
                for simbolo in reversed(producao):
                    pilha.append(simbolo)
            else:
                return False

    return len(tokens) == 0 or tokens == ["$"]

# ------------------------------
#            Testes
# ------------------------------

testes = {
    "int id ;": ["int", "id", ";"],                       # Válida
    "float id , id ;": ["float", "id", ",", "id", ";"],   # Válida
    "int id ; char id ;": ["int", "id", ";", "char", "id", ";"],  # Válida
    "int ;": ["int", ";"]                                # Inválida
}

for descricao, tokens in testes.items():
    resultado = analisador(tokens[:]) 
    print(f"{descricao:<20} → {'Aceita' if resultado else 'Rejeita'}")
