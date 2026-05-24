#Adjancy Matrix

class Graph:
    def __init__(self,vertices):
        #Total number of vertices
        self.V=vertices

        #create adjancy matrix with all 0s
        self.matrix = [[0 for _ in range(vertices)]
                       for _ in range(vertices)]
        
        ## ADD EDGE BETWEEN TWO VERTICES
    def add_edge(self,u,v):   #(0,1)  (0,2)
        self.matrix[u][v] =1
        self.matrix[v][u] =1    #For undirected graph

    def remove_edge(self,u,v):   #(0,1)  (0,2)
        self.matrix[u][v] =0
        self.matrix[v][u] =0    
        


    def display(self):
        for row in self.matrix:
            print(row)

#craete graph with 4 vertices
g=Graph(4)


#add edges
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.display()
print("-------------------------------------------------------------")
g.remove_edge(0,1)
g.display()