fila = []

# Enfilera
def enfileirar(item):
    fila.append(item)

#Desenfilera
def desenfileirar():
    if not fila:  # Se for vazia
        return None
    return fila.pop(0)


class Solution(object):
    def bfs(self, grafo, inicio):
        visitado = [False] * len(grafo)
        enfileirar(inicio)
        visitado[inicio] = True

        while fila:
            no = desenfileirar()
            for vizinho in grafo[no]:
                if not visitado[vizinho]:
                    visitado[vizinho] = True
                    enfileirar(vizinho)

        return visitado
