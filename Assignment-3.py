import sys
import time
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.edges = [] #List to store edges of the graph
        
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.edges.append([u, v, w])
    
    #Print the path from start to source
    def printPath(self, start, predecessor):
        print (start, end='')
        while(predecessor[start] is not None):
            print ('>', predecessor[start], end='')
            start = predecessor[start]
        print ()
        
    def printResult(self, dist, predecessor):
        print("Vertex   Distance  Path")
        for i in range(self.V):
            print("{0}\t\t{1}\t\t\t".format(i, dist[i]), end='')
            self.printPath(i, predecessor)
    
    #Relaxation Step        
    def relax(self, edges, dist, predecessor):
    	for u, v, w in self.edges:
                if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        predecessor[v] = u
     
   #Bellman Ford Alogrithm
    def BellmanFord(self, src):
        
        start = time.time()
        
        #Initialize distances to all vertices as infinite
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        predecessor = [None] * self.V
 
        #Relax all edges V-1 times
        for i in range(self.V - 1):
            self.relax(self.edges, dist, predecessor)
 
		#Check for negative cycles
        for u, v, w in self.edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print ("Graph contains negative weight cycle")
                        return
                        
        end = time.time()
        print ("Time consumed:",start - end)
        
        # print all distance
        self.printResult(dist, predecessor)
 
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -2)
 
#Print the solution
g.BellmanFord(0)
