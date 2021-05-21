from utils import print_mst

class graph:

    def __init__(self,V_set):
        self.V = V_set
        self.edges = []

    def add_edge(self, v1, v2, cost):
        self.edges.append([v1,v2,cost])

    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])

    def union(self,v1,v2,rank,parent):
        root1 = self.find(parent,v1)
        root2 = self.find(parent,v2)

        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            rank[root2]+=1

    def kruskal_initialization(self):

        mst, parent, rank = [], [], []
        i, j = 0, 0

        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)

        return mst, parent, rank, i, j

    def kruskal(self):

        mst, parent, rank, i, j = self.kruskal_initialization()
        self.edges = sorted(self.edges, key=lambda item: item[2])

        while j < self.V - 1:

            v1, v2, cost = self.edges[i]

            set1 = self.find(parent,v1)
            set2 = self.find(parent,v2)

            if set1 != set2:
                j = j + 1
                mst.append([v1, v2, cost])
                self.union(v1,v2,rank,parent)

            i+=1

        print_mst(mst)



