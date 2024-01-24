class GraphNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        node = GraphNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = GraphNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def delete_edge(self, source, destination):
        current = self.graph[source]
        if current and current.vertex == destination:
            self.graph[source] = current.next
        else:
            while current:
                prev = current
                current = current.next
                if current and current.vertex == destination:
                    prev.next = current.next

        current = self.graph[destination]
        if current and current.vertex == source:
            self.graph[destination] = current.next
        else:
            while current:
                prev = current
                current = current.next
                if current and current.vertex == source:
                    prev.next = current.next

    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
    def get_connected_nodes(self, node):
        temp = self.graph[node]
        while temp:
            print(" -> {}".format(temp.vertex), end="")
            temp = temp.next
            
    
    def get_edge(self, node_name1, node_name2):
        node_index1, node_index2 = None, None

        for i in range(self.V):
            if self.graph[i] and self.graph[i].vertex == node_name1:
                node_index1 = i
                break

        for i in range(self.V):
            if self.graph[i] and self.graph[i].vertex == node_name2:
                node_index2 = i
                break

        if node_index1 is not None and node_index2 is not None:
            current = self.graph[node_index1]
            while current:
                if current.vertex == node_name2:
                    return (node_name1, node_name2)
                current = current.next

        return None
     
    def are_connected(self, node_name1, node_name2):
        node_index1, node_index2 = None, None

        for i in range(self.V):
            if self.graph[i] and self.graph[i].vertex == node_name1:
                node_index1 = i
                break

        for i in range(self.V):
            if self.graph[i] and self.graph[i].vertex == node_name2:
                node_index2 = i
                break

        if node_index1 is not None and node_index2 is not None:
            current = self.graph[node_index1]
            while current:
                if current.vertex == node_name2:
                    return True
                current = current.next

        return False
    
    def is_valid_path(self, path):
        for i in range(len(path) - 1):
            if not self.are_connected(path[i], path[i + 1]):
                return False
        return True



if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)

    print("Original Graph:")
    graph.print_graph()

    # Delete an edge
    graph.delete_edge(0, 1)
    print("\nGraph after deleting edge (0, 1):")
    graph.print_graph()

    # Get connected nodes for node 0
    connected_nodes = graph.get_connected_nodes(0)
    print("Connected nodes for node 0:", connected_nodes)

    # Get an edge between nodes 0 and 1
    edge_0_1 = graph.get_edge(0, 1)
    print("Edge between nodes 0 and 1:", edge_0_1)

    # Check if nodes 0 and 1 are connected
    connected_0_1 = graph.are_connected(0, 1)
    print("Nodes 0 and 1 are connected:", connected_0_1)

    # Check if a path is valid
    path1 = [3, 4, 0]  # Valid path
    valid_path1 = graph.is_valid_path(path1)
    print("Is path1 valid?", valid_path1)
