# Algoritmo de Kruskal com union-find

## Entrada

- Na primeira linha temos dois números inteiros, *V* e *E*. Sendo *V* o número de vértices e *E* o número de arestas do grafo;
- Depois, teremos *E* linhas, que representam as arestas do grafo, sendo cada aresta composta por três inteiros: **v1**, **v2**, **w**;
- **v1** e **v2** são os vértices conectados pela aresta e **w** é o peso da aresta.


- Abaixo temos um exemplo de grafo com 9 vértices e 13 arestas, presente no arquivo `input.in`:
```
9 13
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 8 12
2 5 4
3 4 9
3 5 14
4 5 2
5 6 10
6 7 9
7 8 6
```

## Saída

- A saída retorna a árvore de abrangência mínima do grafo (MST - Minimum Spanning Tree);
- Com o exemplo presente no arquivo `input.in`, temos a seguinte saída:

```
MST construída
v1 -- v2 == peso
4 -- 5 == 2
0 -- 1 == 4
2 -- 5 == 4
7 -- 8 == 6
2 -- 3 == 7
0 -- 7 == 8
1 -- 2 == 8
6 -- 7 == 9
Custo: 48
```

## Executar

```
./kruskal < input.in
```

## Complexidade

- O algoritmo possui uma complexidade aproximada de `O(ElogE)` ou `O(ElogV)`.