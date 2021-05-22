# Algoritmo de Prim

## Entrada

- Na primeira linha temos dois números inteiros, *V* e *E*. Sendo *V* o número de vértices e *E* o número de arestas do grafo;
- Depois, teremos *E* linhas, que representam as arestas do grafo, sendo cada aresta composta por três inteiros: **v1**, **v2**, **wt**;
- **v1** e **v2** são os vértices conectados pela aresta e **wt** é o peso da aresta;
- Vale ressaltar que para o funcionamento correto do algoritmo, a entrada deve ser composta por vértices com valores de 0 a *V* - 1;

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
Constructed MST:
0 - 1
1 - 2
2 - 3
5 - 4
2 - 5
7 - 6
0 - 7
7 - 8
```

## Executar

- A execução pode ser feita tanto de forma interativa pelo terminal, como por um arquivo de texto:

```
./prim < input.in
```

## Complexidade

- O algoritmo possui uma complexidade aproximadamente de `O(ElogV)`;
