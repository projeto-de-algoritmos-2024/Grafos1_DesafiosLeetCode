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
    def bfs_colore(self, grafo, inicio):
        cor = [-1] * len(grafo)
        enfileirar(inicio)
        cor[inicio] = 0

        while fila:
            no = desenfileirar()
            for vizinho in grafo[no]:
                if cor[vizinho] == -1:
                    cor[vizinho] = 1 - cor[no]  # Atribui cor alternada
                    enfileirar(vizinho)

        return cor
    
print(Solution().bfs_colore([[1, 3], [0, 2], [1, 3], [0, 2]], 0))