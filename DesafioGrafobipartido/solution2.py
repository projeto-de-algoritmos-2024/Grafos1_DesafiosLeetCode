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
    def bfs_verifica_conflitos(self, grafo, inicio):
        cor = [-1] * len(grafo)
        enfileirar(inicio)
        cor[inicio] = 0

        while fila:
            no = desenfileirar()
            for vizinho in grafo[no]:
                if cor[vizinho] == -1:
                    cor[vizinho] = 1 - cor[no]  # Atribui cor alternad
                    enfileirar(vizinho)
                elif cor[vizinho] == cor[no]:
                    return False  # Conflito encontrado, não é bipartido

        return True
