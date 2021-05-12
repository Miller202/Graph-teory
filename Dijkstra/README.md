# Algoritmo de Dijkstra

## Entrada

- Na primeira linha temos dois números inteiros, *V* e *E*. Sendo *V* o número de vértices e *E* o número de arestas do grafo;
- Depois, teremos *E* linhas, que representam as arestas do grafo, sendo cada aresta composta por três inteiros: **v1**, **v2**, **wt**;
- **v1** e **v2** são os vértices conectados pela aresta e **wt** é o peso da aresta;
- Vale ressaltar que para o funcionamento correto do algoritmo, a entrada deve ser composta por vértices com valores de 0 a *V* - 1;

- Abaixo temos um exemplo de grafo com 9 vértices e 12 arestas, presente no arquivo `input.in`:
```
9 12
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 8 6
2 5 4
3 4 9
4 5 2
5 6 10
6 7 9
7 8 6
```

## Saída

- A saída retorna à esquerda os vértices e na direita as suas respectivas distâncias da origem;
- Com o exemplo de grafo presente no arquivo `input.in`, temos a seguinte saída:

```
Vertex  - Distance from src
   0    -        0
   1    -        4
   2    -        12
   3    -        19
   4    -        18
   5    -        16
   6    -        17
   7    -        8
   8    -        14
```

## Executar

- A execução pode ser feita tanto de forma interativa pelo terminal, como por um arquivo de texto:

```
./dijkstra < input.in
```

## Complexidade

- O algoritmo possui uma complexidade aproximadamente de `n log n`;
