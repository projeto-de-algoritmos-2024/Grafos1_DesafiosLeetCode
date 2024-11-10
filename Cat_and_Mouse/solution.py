from collections import deque

# rodadas
RAT_TURN = 0
CAT_TURN = 1
# resultados
RAT_WIN = 1
CAT_WIN = 2
DRAW = 0

class Solution(object):

    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)

        # Dicionário para armazenar os resultados dos estados (pos_rato, pos_gato, rodada) -> resultado
        # Incialmente, somente os casos base são preenchidos
        results = {}
        for i in range(1, n):
            # O rato ganha se chegar ao nó 0, independente da posição do gato
            results[0, i, CAT_TURN] = results[0, i, RAT_TURN] = RAT_WIN
            # O gato ganha se estiver no mesmo nó que o rato
            results[i, i, CAT_TURN] = results[i, i, RAT_TURN] = CAT_WIN

        # Todos os possíveis estados e seus graus
        # (pos_rato,pos_gato, rodada) -> número de próximos estados
        degrees = {}
        for rat in range(1, n):
            for cat in range(1, n):
                # Se é a vez do rato, ele pode ir para qualquer vizinho
                degrees[rat, cat, RAT_TURN] = len(graph[rat])
                # Se é a vez do gato, ele pode ir para qualquer vizinho, exceto o nó 0
                degrees[rat, cat, CAT_TURN] = len(
                    graph[cat]) - int(0 in graph[cat])

        # Inicializa a fila com os estados que já foram preenchidos
        q = deque([estado for estado in results.keys()])
        print(q)

        # Inicializa o BFS
        # Enquanto houver estados na fila, calcula o resultado de seus estados anteriores
        # As primeiras iterações serão para os casos base, que já estão no vetor de resultados
        # O Objetivo desta BFS é atribuir o resultado para o estado (1,2,RAT_TURN), que é o estado inicial.
        # para isso, ela encontra o menor caminho entre o estado inicial e algum caso base.
        while q:
            rat, cat, turn = q.popleft()
            current_result = results[rat, cat, turn]

            prev_states = []
            if turn == RAT_TURN:
                # Se é a vez do rato, então o gato moveu por último
                for prev_cat in graph[cat]:
                    prev_states.append((rat, prev_cat, CAT_TURN))
            else:
                # Se é a vez do gato, então o rato moveu por último
                for prev_rat in graph[rat]:
                    prev_states.append((prev_rat, cat, RAT_TURN))

            # Para cada estado anterior, calcula o resultado
            for prev_state in prev_states:
                prev_rat, prev_cat, prev_turn = prev_state
                if prev_state in results or prev_cat == 0:
                    # Se o resultado do estado anterior já foi calculado ou o gato está no nó 0, pula
                    continue

                degrees[prev_state] -= 1 # um dos vizinhos do estado anteriore foi visitado
                is_winner = ((current_result == RAT_WIN and prev_turn == RAT_TURN) or (
                    current_result == CAT_WIN and prev_turn == CAT_TURN))

                if is_winner or (degrees[prev_state] == 0):
                    # Se o jogador que moveu por último ganhou ou não há mais movimentos possíveis, o resultado deste estado é definido
                    results[prev_state] = current_result
                    q.append(prev_state)

        return results.get((1, 2, RAT_TURN), DRAW)
