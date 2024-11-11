class Solution(object):
    def contarNosVisitados(self, arestas):
        n = len(arestas)
        contagens = [0] * n  # Armazena o número de nós visitados a partir de cada nó
        visitado = [0] * n  # 0 = não visitado, 1 = visitando, 2 = visitado

        for i in range(n):
            if contagens[i] == 0:
                nos_do_caminho = {}
                pilha = []
                no = i
                indice = 0
                while True:
                    if visitado[no] == 2:
                        total = contagens[no]
                        for idx in range(len(pilha) - 1, -1, -1):
                            total += 1
                            contagens[pilha[idx]] = total
                            visitado[pilha[idx]] = 2
                        break
                    if visitado[no] == 1:
                        # Encontramos um ciclo
                        indice_inicio_ciclo = nos_do_caminho[no]
                        comprimento_ciclo = len(pilha) - indice_inicio_ciclo
                        # Atribui o comprimento do ciclo aos nós do ciclo
                        for idx in range(indice_inicio_ciclo, len(pilha)):
                            contagens[pilha[idx]] = comprimento_ciclo
                            visitado[pilha[idx]] = 2
                        # Propaga os valores para os nós antes do ciclo
                        for idx in range(indice_inicio_ciclo - 1, -1, -1):
                            contagens[pilha[idx]] = contagens[pilha[idx + 1]] + 1
                            visitado[pilha[idx]] = 2
                        break
                    else:
                        visitado[no] = 1  # Marca como visitando
                        nos_do_caminho[no] = indice
                        pilha.append(no)
                        indice += 1
                        no = arestas[no]
        return contagens

solucao = Solution()
arestas = [1, 2, 0, 4, 5, 3]
print(solucao.contarNosVisitados(arestas))
