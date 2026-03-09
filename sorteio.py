import random

grupo = {
    1: "Samuel",
    2: "Pedro",
    3: "Ian",
    4: "Mathues",
    5: "Marcos",
    6: "Davi",
    7: "Renan",
    8: "Bruno",
    9: "Murilo",
    10: "Edson"
}

nomes = list(grupo.values())

random.shuffle(nomes)

grupo1 = nomes[:5]
grupo2 = nomes[5:]

print("Grupo 1:")
for pessoa in grupo1:
    print("-", pessoa)

print("\nGrupo 2:")
for pessoa in grupo2:
    print("-", pessoa)