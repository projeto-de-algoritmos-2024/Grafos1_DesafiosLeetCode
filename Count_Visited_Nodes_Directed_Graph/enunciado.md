Existe um grafo direcionado que consiste em nós numerados de \(0\) a \(n - 1\) e \(n\) arestas direcionadas.

Você recebe uma matriz indexada \(0\) chamada `edges`, onde `edges[i]` indica que há uma aresta do nó \(i\) ao nó `edges[i]`.

Considere o seguinte processo no grafo:

Você começa em um nó \(x\) e continua visitando outros nós através de arestas até chegar a um nó que você já visitou antes neste mesmo processo.

Retorne uma matriz `answer` onde `answer[i]` é o número de nós diferentes que você visitará se executar o processo começando pelo nó \(i\).
