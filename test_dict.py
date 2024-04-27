

lista = [1,2,3,4,5,6,7]

k = 3

def funcao(lista, k):
    i = 0
    measure = len(lista)
    for _ in range(k):
        
        lista = [lista[measure-1]] + lista
        lista = lista.pop()
        #print(lista)
    return lista


variavel = funcao(lista, k)
print(variavel)
