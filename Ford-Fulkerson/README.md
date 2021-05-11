# Algoritmo de Ford-Fulkerson

## Entrada

- Na primeira linha temos dois números inteiros, *V* e *E*. Sendo *V* o número de vértices e *E* o número de arestas do grafo;
- Na segunda linha temos dois inteiros, *begin* e *end*. Sendo *begin* o vértice de origem e *end* o vértice de destino;
- Depois, teremos *E* linhas, que representam as arestas do grafo, sendo cada aresta composta por três inteiros: **v1**, **v2**, **cap**;
- **v1** e **v2** são os vértices conectados pela aresta e **cap** é a capacidade da aresta;
- Vale ressaltar que para o funcionamento correto do algoritmo, a entrada deve ser composta por vértices com valores de 0 a *V* - 1;

- Abaixo temos um exemplo de grafo com 6 vértices e 10 arestas, presente no arquivo `input.in`:
```
6 10
0 5
0 1 5
0 2 7
1 2 3
1 3 8
2 1 6
2 5 9
3 2 1
3 5 4
4 3 2
4 5 9
```

## Saída

- A saída retorna o fluxo máximo do grafo a partir do algoritmo de Ford-Fulkerson;
- Com o exemplo presente no arquivo `input.in`, temos a seguinte saída:

```
Max Flow: 12
```

## Executar

- A execução pode ser feita tanto de forma interativa pelo terminal, como por um arquivo de texto:

```
./ford_fulkerson < input.in
```

## Complexidade

- O algoritmo possui uma complexidade aproximadamente de `n log n`;
