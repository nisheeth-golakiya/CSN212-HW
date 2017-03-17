import sys
import time
class Graph:

    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.edges = [] #List to store edges of the graph

    #function to add an edge to graph
    def addEdge(self,u,v,w):
        self.edges.append([u, v, w])

    #Print the path from start to source
    #

    #Relaxation Step
    def relax(self, edges, dist, predecessor):
        for u, v, w in self.edges:
                if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        predecessor[v] = u

   #Bellman Ford Alogrithm
    def BellmanFord(self, src):

        start = time.clock()

        #Initialize distances to all vertices as infinite
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        predecessor = [None] * self.V

        #Relax all edges V-1 times
        for i in range(self.V - 1):
            self.relax(self.edges, dist, predecessor)
	
        end = time.clock()
        print ("Time consumed:",end - start)
	
    #Check for negative cycles
        for u, v, w in self.edges:
                if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                        print ("Graph contains negative weight cycle")
                        return
        
	#Print the result
	self.printResult(dist, predecessor)
	
V, E = [int(x) for x in input().split()]
graph = Graph(V)
for i in range(E):
    src, dest, weight = [int(x) for x in input().split()]
    graph.addEdge(src, dest, weight)

#Print the solution
graph.BellmanFord(0)
