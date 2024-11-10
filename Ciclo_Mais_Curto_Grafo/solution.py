fila = []

# Enfileira
def enfileirar(item):
    fila.append(item)

# Desenfileira
def desenfileirar():
    if not fila:
        return None
    return fila.pop(0)

class Solution(object):
    def findShortestCycle(self, n, arestas):
        # Construir o grafo como lista de adjacência
        grafo = [[] for _ in range(n)]
        for u, v in arestas:
            grafo[u].append(v)
            grafo[v].append(u)

        comprimento_min_ciclo = float('inf')

        for inicio in range(n):
            dist = [-1] * n
            pai = [-1] * n
            dist[inicio] = 0

            # Limpar a fila antes de cada BFS
            global fila
            fila = []
            enfileirar(inicio)

            while fila:
                u = desenfileirar()
                for v in grafo[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        pai[v] = u
                        enfileirar(v)
                    elif pai[u] != v:
                        # Ciclo detectado
                        comprimento_ciclo = dist[u] + dist[v] + 1
                        comprimento_min_ciclo = min(comprimento_min_ciclo, comprimento_ciclo)

        return comprimento_min_ciclo if comprimento_min_ciclo != float('inf') else -1