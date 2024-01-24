class Node:
    def __init__(self, id, heuristic_value):
        self.id = id
        self.heuristic_value = heuristic_value
        self.cost = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.cost + self.heuristic_value < other.cost + other.heuristic_value

def a_star_search(graph, start_node, destination_node, heuristic_values):
    """Finds the shortest path from the start node to the destination node in the given graph using the A* algorithm.

    Args:
        graph: A dictionary mapping node IDs to lists of neighboring node IDs and edge costs.
        start_node: The ID of the start node.
        destination_node: The ID of the destination node.
        heuristic_values: A dictionary mapping node IDs to heuristic values.

    Returns:
        A list of node IDs representing the shortest path from the start node to the destination node, or None if no path exists.
    """

    priority_queue = []
    start_node = Node(start_node, heuristic_values[start_node])
    start_node.cost = 0
    priority_queue.append(start_node)

    while priority_queue:
        current_node = priority_queue.pop(0)

        if current_node.id == destination_node:
            path = []
            while current_node is not None:
                path.append(current_node.id)
                current_node = current_node.parent
            path.reverse()
            return path

        for neighbor_id, edge_cost in graph[current_node.id]:
            neighbor_node = Node(neighbor_id, heuristic_values[neighbor_id])

            new_cost = current_node.cost + edge_cost
            if new_cost < neighbor_node.cost:
                neighbor_node.cost = new_cost
                neighbor_node.parent = current_node

                if neighbor_node not in priority_queue:
                    priority_queue.append(neighbor_node)
                    priority_queue.sort()

    return None

graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2), ('A', 6)],
    'C': [('D', 5), ('E', 5), ('B', 3)],
    'D': [('E', 8), ('C', 1), ('B', 2)],
    'E': [('I', 5), ('J', 5), ('C', 5), ('D', 8)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('G', 3), ('H', 2), ('E', 5), ('J', 3)],
    'J': [('I', 3), ('E', 5)],
}

heuristic_values = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0,
}

# Example usage:

# Your graph remains the same

start_node = 'A'
destination_node = 'J'

path = a_star_search(graph, start_node, destination_node, heuristic_values)

if path is None:
    print('No path found from {} to {}.'.format(start_node, destination_node))
else:
    print('The shortest path from {} to {} is:'.format(start_node, destination_node))
    print(path)

# class Node:
#     def __init__(self, id, heuristic_value):
#         self.id = id
#         self.heuristic_value = heuristic_value
#         self.cost = float('inf')
#         self.parent = None

#     def __lt__(self, other):
#         return self.cost + self.heuristic_value < other.cost + other.heuristic_value

# def a_star_search(graph, start_node, destination_node):
#     """Finds the shortest path from the start node to the destination node in the given graph using the A* algorithm.

#     Args:
#         graph: A dictionary mapping node IDs to lists of neighboring node IDs and edge costs.
#         start_node: The ID of the start node.
#         destination_node: The ID of the destination node.

#     Returns:
#         A list of node IDs representing the shortest path from the start node to the destination node, or None if no path exists.
#     """

#     priority_queue = []
#     start_node = Node(start_node, heuristic_value=0)  # Set heuristic_value to 0 for the start node
#     start_node.cost = 0  # Initialize the cost for the start node
#     priority_queue.append(start_node)

#     while priority_queue:
#         current_node = priority_queue.pop(0)

#         if current_node.id == destination_node:
#             path = []
#             while current_node is not None:
#                 path.append(current_node.id)
#                 current_node = current_node.parent
#             path.reverse()
#             return path

#         for neighbor_id, edge_cost in graph[current_node.id]:
#             neighbor_node = Node(neighbor_id, heuristic_value=0)  # Set heuristic_value to 0 initially

#             new_cost = current_node.cost + edge_cost
#             if new_cost < neighbor_node.cost:
#                 neighbor_node.cost = new_cost
#                 neighbor_node.parent = current_node

#                 # Calculate the heuristic value for the neighbor based on its ID and the destination node
#                 neighbor_node.heuristic_value = calculate_heuristic(neighbor_id, destination_node)

#                 if neighbor_node not in priority_queue:
#                     priority_queue.append(neighbor_node)
#                     priority_queue.sort()  # Sort the queue based on the total cost

#     return None

# huresitic_values = {
#     'A': 10,
#     'B': 8,
#     'C': 5,
#     'D': 7,
#     'E': 3,
#     'F': 6,
#     'G': 5,
#     'H': 3,
#     'I': 1,
#     'J': 0,
# }

# # Example usage:

# graph = {
#     'A': [('B', 6), ('F', 3)],
#     'B': [('C', 3), ('D', 2), ('A', 6)],
#     'C': [('D', 5), ('E', 5), ('B', 3)],
#     'D': [('E', 8), ('C', 1), ('B', 2)],
#     'E': [('I', 5), ('J', 5), ('C', 5), ('D', 8)],
#     'F': [('A', 3), ('G', 1), ('H', 7)],
#     'G': [('F', 1), ('I', 3)],
#     'H': [('F', 7), ('I', 2)],
#     'I': [('G', 3), ('H', 2), ('E', 5), ('J', 3)],
#     'J': [('I', 3), ('E', 5)],
# }

# start_node = 'A'
# destination_node = 'J'

# path = a_star_search(graph, start_node, destination_node)

# if path is None:
#     print('No path found from {} to {}.'.format(start_node, destination_node))
# else:
#     print('The shortest path from {} to {} is:'.format(start_node, destination_node))
#     print(path)
