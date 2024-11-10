Há um gráfico **bidirecional** com `n`vértices, onde cada vértice é rotulado de `0`a `n - 1`. As arestas no gráfico são representadas por um dado array de inteiros 2D `edges`, onde denota uma aresta entre vértice e vértice . Cada par de vértices é conectado por no máximo uma aresta, e nenhum vértice tem uma aresta para si mesmo.`edges[i] = [ui, vi]uivi`

Retorna *o comprimento do ciclo **mais curto** no gráfico* . Se não existir nenhum ciclo, retorna `-1`.

Um ciclo é um caminho que começa e termina no mesmo nó, e cada aresta do caminho é usada apenas uma vez.