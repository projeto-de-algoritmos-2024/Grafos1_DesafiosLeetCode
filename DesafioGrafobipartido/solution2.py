fila = []

# Enfilera


def enfileirar(item):
    fila.append(item)

# Desenfilera


def desenfileirar():
    if not fila:  # Se for vazia
        return None
    return fila.pop(0)


class Solution(object):
    def isBipartite(self, grafo):
        cor = [-1] * len(grafo)

        for inicio in range(len(grafo)):
            if cor[inicio] == -1:
                enfileirar(inicio)
                cor[inicio] = 0

                while fila:
                    no = desenfileirar()
                    for vizinho in grafo[no]:
                        if cor[vizinho] == -1:
                            cor[vizinho] = 1 - cor[no] # Atribui cor alternad
                            enfileirar(vizinho)
                        elif cor[vizinho] == cor[no]:
                            return False # Conflito encontrado, não é bipartido
        return True 
