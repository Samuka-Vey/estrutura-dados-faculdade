lista = [1,5,9,3, 3, 800, 10, 12, -1, -1150]
v_maior = lista[0]

for i in range(len(lista)):
    v_atual = lista[i]
    if v_atual < v_maior:
        v_maior = v_atual
    
    
print(v_maior)