## Problema: Verificação de Grafo Bipartido

Dado um **grafo não direcionado** com `n` nós, onde cada nó é numerado entre `0` e `n - 1`. Você recebe um array 2D `graph`, onde `graph[u]` é um array de nós aos quais o nó `u` é adjacente. Mais formalmente, para cada `v` em `graph[u]`, existe uma aresta não direcionada entre o nó `u` e o nó `v`.

O grafo possui as seguintes propriedades:

- Não há **arestas próprias**: `graph[u]` **não** contém `u`.
- Não há **arestas paralelas**: `graph[u]` **não** contém valores duplicados.
- Se `v` está em `graph[u]`, então `u` está em `graph[v]` (o grafo é **não direcionado**).
- O grafo pode **não estar conectado**, o que significa que pode haver dois nós `u` e `v` sem um caminho entre eles.

### Definição de Grafo Bipartido

Um grafo é **bipartido** se seus nós podem ser divididos em dois conjuntos independentes `A` e `B` de tal forma que **cada** aresta no grafo conecta um nó no conjunto `A` com um nó no conjunto `B`.

### Objetivo

Retorne `true` se e somente se o grafo for **bipartido**.
