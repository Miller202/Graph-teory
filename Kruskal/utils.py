def print_mst(mst):
    current_cost = 0
    print("MST construída:")
    print("V1 -- V2 == peso")
    for v1,v2,cost in mst:
        current_cost += cost
        print("%d -- %d == %d" % (v1,v2,cost))

    print("O custo final da menor árvore geradora é de:", current_cost)