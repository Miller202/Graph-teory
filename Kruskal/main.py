from kruskal_mst import graph

def main():
    input = open("input.txt", "r")

    V_A = input.readline().split()
    n_V, n_A = int(V_A[0]), int(V_A[1])
    grafo = graph(n_V)

    for i in range(n_A):
        aresta = input.readline().split()
        v1 = int(aresta[0])
        v2 = int(aresta[1])
        cost = int(aresta[2])

        grafo.add_edge(v1, v2, cost)

    input.close()

    grafo.kruskal()

if __name__ == '__main__':
    main()



