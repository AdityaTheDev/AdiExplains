class DirectedGraph:
    def __init__(self):
        # Dictionary to store adjacency list
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a vertex if it doesn't already exist
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, undir=False):
        # Add an edge from u to v
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        
        if undir==True:
            self.graph[v].append(u)
        

    def display_graph(self):
        # Display the adjacency list representation of the graph
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, edges))}")

# Example usage:
if __name__ == "__main__":
    dg = DirectedGraph()
    dg.add_edge(1, 2,True)
    dg.add_edge(2, 3,True)
    dg.add_edge(3, 4,True)


    print("Directed Graph:")
    dg.display_graph()
