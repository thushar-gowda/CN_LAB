class Graph():

    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]
                    for row in range(vertices)]
        
    def printSolution(self,parent):
        minimumCost = 0
        print("Edge \t Weight")
        for i in range(1, self.V):
            minimumCost = minimumCost + self.graph[i][parent[i]]
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
        print("Minimum Spanning Tree", minimumCost)

    def minDistance(self,dist,sptSet):
        min = 1e7
        for v in range(self.V):
            if (dist[v]<min and sptSet[v]==False) :
                min = dist[v]
                min_index = v
        return min_index

    def PrimMST(self):
        dist = [1e7]*self.V
        parent = [0]*self.V
        sptSet = [False]*self.V
        dist[0] = 0
        parent[0] = -1
        for cout in range(self.V):
            u = self.minDistance(dist,sptSet)
            sptSet[u]=True
            for v in range(self.V):
                if (self.graph[u][v]>0 and sptSet[v]==False and dist[v]>self.graph[u][v]):
                    dist[v]=self.graph[u][v]
                    parent[v]=u
        self.printSolution(parent)

g=Graph(5)
g.graph=[[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
g.PrimMST()
