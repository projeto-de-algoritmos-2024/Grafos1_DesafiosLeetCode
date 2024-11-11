class Solution(object):
    def contarNosVisitados(self, arestas):
        n = len(arestas)
        contagens = [0] * n

        for i in range(n):
            visitado = set()
            no = i
            while no not in visitado:
                visitado.add(no)
                no = arestas[no]
            contagens[i] = len(visitado)
        return contagens

solucao = Solution()
arestas = [1, 2, 0, 4, 5, 3]
print(solucao.contarNosVisitados(arestas))