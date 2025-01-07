class Graph:
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
            
    def bfs(self, start_vertex):

        if start_vertex not in self.graph:
            print(f"Vertex {start_vertex} not found in the graph!")
            return

        visited = set()  # Totrack visited vertices
        queue = [start_vertex]  #Queue for BFS

        print("BFS Traversal:", end=" ")
        while queue:
            vertex = queue.pop(0)  #Dequeue a vertex
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                #Add all unvisited neighbors to the queue
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()
            
    def search_target_using_bfs(self, source, target):
    
        if source not in self.graph:
            print(f"Source vertex {source} not found in the graph!")
            return False
        if target not in self.graph:
            print(f"Target vertex {target} not found in the graph!")
            return False

        visited = set()  #To track visited vertices
        queue = [source]  #Queue for BFS

        while queue:
            vertex = queue.pop(0)  #Dequeue a vertex
            if vertex == target:
                print(f"Target {target} found starting from {source}!")
                return True
            if vertex not in visited:
                visited.add(vertex)

                #Add all unvisited neighbors to the queue
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        print(f"Target {target} not reachable from {source}.")
        return False
        

    def display_graph(self):
        # Display the adjacency list representation of the graph
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, edges))}")

# Example usage:
if __name__ == "__main__":
    dg = Graph()
    dg.add_edge(1, 2,True)
    dg.add_edge(2, 3,True)
    dg.add_edge(2, 4,True)
    dg.add_edge(3, 5,True)
    dg.add_edge(4, 5,True)
    dg.add_edge(5, 6,True)


    dg.search_target_using_bfs(1,9)

