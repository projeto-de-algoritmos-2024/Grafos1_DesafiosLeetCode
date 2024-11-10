class Solution(object):
    def bfs_com_distancias(self, n, arestas, inicio):
        # Construir o grafo
        grafo = [[] for _ in range(n)]
        for u, v in arestas:
            grafo[u].append(v)
            grafo[v].append(u)

        dist = [-1] * n
        fila = []
        fila.append(inicio)
        dist[inicio] = 0

        while fila:
            u = fila.pop(0)
            for v in grafo[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    fila.append(v)

        return dist
    
#Caso de teste
solucao = Solution()
n = 5
arestas = [[0,1],[0,2],[1,3],[1,4]]
inicio = 0
print(solucao.bfs_com_distancias(n, arestas, inicio))