from heapq import heappop, heappush

class Node:
    def __init__(self, state, cost, parent=None):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def uniform_cost_search(graph, start, goal):
    """
    Uniform Cost Search algorithm

    Args:
        graph: A directed graph represented as a dictionary of dictionaries, where the keys are the nodes and the values are dictionaries of adjacent nodes and their costs
        start: The start node
        goal: The goal node

    Returns:
        A list of nodes representing the shortest path from the start node to the goal node, or None if no path is found
    """

    open_list = []
    closed_list = set()

    heappush(open_list, Node(start, 0))

    while open_list:
        node = heappop(open_list)

        if node.state == goal:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            path.reverse()
            return path

        if node.state in closed_list:
            continue

        closed_list.add(node.state)

        for neighbor in graph[node.state]:
            cost = node.cost + graph[node.state][neighbor]
            new_node = Node(neighbor, cost, node)
            heappush(open_list, new_node)

    return None

# Example usage:

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 2},
    'C': {'D': 1},
    'D': {'E': 4},
    'E': {'G': 1},
}

start = 'A'
goal = 'G'

path = uniform_cost_search(graph, start, goal)

if path:
    print(f'The shortest path from {start} to {goal} is: {path}')
else:
    print('No path found')


# class Node:
#     def _init_(self, id, cost, parent=None, is_visited=False, neighbors=None):
#         self.id = id
#         self.cost = cost
#         self.parent = parent
#         self.is_visited = is_visited
#         self.neighbors = neighbors

#     def _lt_(self, other):
#         return self.cost < other.cost


# class PriorityQueue:
#     def _init_(self):
#         self.queue = []

#     def enqueue(self, node):
#         self.queue.append(node)
#         self.queue.sort(reverse=True)

#     def dequeue(self):
#         return self.queue.pop()

#     def is_empty(self):
#         return len(self.queue) == 0


# def uniform_cost_search(graph, source, destination):
#     queue = PriorityQueue()
#     queue.enqueue(Node(source, 0))

#     while not queue.is_empty():
#         node = queue.dequeue()

#         if node.id == destination:
#             return reconstruct_path(node)

#         if not node.is_visited:
#             node.is_visited = True

#             for neighbor in node.neighbors:
#                 queue.enqueue(Node(neighbor, node.cost + 1, node))

#     return None


# def reconstruct_path(node):
#     path = []

#     while node:
#         path.append(node.id)
#         node = node.parent

#     path.reverse()
#     return path


# graph = {
#     0: [1, 2],
#     1: [3, 4],
#     2: [5, 6],
#     3: [7],
#     4: [8],
#     5: [9],
#     6: [10]
# }

# source = 0
# destination = 10

# path = uniform_cost_search(graph, source, destination)

# if path:
#     print(path)
# else:
#     print("The destination node is not reachable.")


# graph = {
#     0: [1, 2],
#     1: [3, 4],
#     2: [5, 6],
#     3: [7],
#     4: [8],
#     5: [9],
#     6: [10],
#     11: []
# }

# source = 0
# destination = 11

# path = uniform_cost_search(graph, source, destination)

# if path:
#     print(path)
# else:
#     print("The destination node is not reachable.")
# # class Node:
# #     def __init__(self, id, cost, parent=None):
# #         self.id = id
# #         self.cost = cost
# #         self.parent = parent

# #     def __lt__(self, other):
# #         return self.cost < other.cost

# # def uniform_cost_search(graph, start_node, destination_node):
# #     """Finds the shortest path from the start node to the destination node in the given graph using the Uniform Cost Search algorithm.

# #     Args:
# #         graph: A dictionary mapping node IDs to lists of neighboring node IDs and costs.
# #         start_node: The ID of the start node.
# #         destination_node: The ID of the destination node.

# #     Returns:
# #         A list of node IDs representing the shortest path from the start node to the destination node, or None if no path exists.
# #     """

# #     priority_queue = []
# #     start_node = Node(start_node, 0)
# #     priority_queue.append(start_node)

# #     while priority_queue:
# #         current_node = priority_queue.pop(0)

# #         if current_node.id == destination_node:
# #             path = []
# #             while current_node is not None:
# #                 path.append(current_node.id)
# #                 current_node = current_node.parent
# #             path.reverse()
# #             return path

# #         for neighbor_id, cost in graph[current_node.id].items():
# #             neighbor_node = Node(neighbor_id, cost + current_node.cost, current_node)

# #             if neighbor_node not in priority_queue:
# #                 priority_queue.append(neighbor_node)
# #             elif neighbor_node.cost > cost + current_node.cost:
# #                 neighbor_node.cost = cost + current_node.cost
# #                 neighbor_node.parent = current_node

# #     return None

# # # Example usage:

# # graph = {}

# # # Add nodes and their neighbors to the graph
# # graph['A'] = [('B', 6), ('F', 3)]
# # graph['B'] = [('C', 3), ('D', 2), ('A', 6)]
# # graph['C'] = [('D', 5), ('E', 5), ('B', 3)]
# # graph['D'] = [('E', 8), ('C', 1), ('B', 2)]
# # graph['E'] = [('I', 5), ('J', 5), ('C', 5), ('D', 8)]
# # graph['F'] = [('A', 3), ('G', 1), ('H', 7)]
# # graph['G'] = [('F', 1), ('I', 3)]
# # graph['H'] = [('F', 7), ('I', 2)]
# # graph['I'] = [('G', 3), ('H', 2), ('E', 5), ('J', 3)]
# # graph['J'] = [('I', 3), ('E', 5)]

# # start_node = 'A'
# # destination_node = 'J'

# # path = uniform_cost_search(graph, start_node, destination_node)

# # if path is None:
# #     print('No path found from {} to {}.'.format(start_node, destination_node))
# # else:
# #     print('The shortest path from {} to {} is:'.format(start_node, destination_node))
# #     print(path)


# # # class Node:
# # #     def __init__(self, id, cost, parent=None):
# # #         self.id = id
# # #         self.cost = cost
# # #         self.parent = parent

# # #     def __lt__(self, other):
# # #         return self.cost < other.cost

# # # def uniform_cost_search(graph, start_node, destination_node):
# # #     """Finds the shortest path from the start node to the destination node in the given graph using the Uniform Cost Search algorithm.

# # #     Args:
# # #         graph: A dictionary mapping node IDs to lists of neighboring node IDs and costs.
# # #         start_node: The ID of the start node.
# # #         destination_node: The ID of the destination node.

# # #     Returns:
# # #         A list of node IDs representing the shortest path from the start node to the destination node, or None if no path exists.
# # #     """

# # #     priority_queue = []
# # #     start_node = Node(start_node, 0)
# # #     priority_queue.append(start_node)

# # #     while priority_queue:
# # #         current_node = priority_queue.pop(0)

# # #         if current_node.id == destination_node:
# # #             path = []
# # #             while current_node is not None:
# # #                 path.append(current_node.id)
# # #                 current_node = current_node.parent
# # #             path.reverse()
# # #             return path

# # #         for neighbor_id, cost in graph[current_node.id].items():
# # #             neighbor_node = Node(neighbor_id, cost + current_node.cost, current_node)

# # #             if neighbor_node not in priority_queue:
# # #                 priority_queue.append(neighbor_node)
# # #             elif neighbor_node.cost > cost + current_node.cost:
# # #                 neighbor_node.cost = cost + current_node.cost
# # #                 neighbor_node.parent = current_node

# # #     return None

# # # # Example usage:

# # # # graph = {
# # # #     'A': {'B': 2, 'F': 3},
# # # #     'B': {'C': 3, 'D': 2},
# # # #     'C': {'D': 5, 'E': 5},
# # # #     'D': {'E': 8},
# # # #     'E': {'I': 5, 'J': 5},
# # # #     'F': {'G': 1},
# # # #     'G': {'I': 3},
# # # #     'I': {'J': 3},
# # # # }
# # # graph = {
# # #     'A': [('B', 6), ('F', 3)],
# # #     'B': [('C', 3), ('D', 2), ('A', 6)],
# # #     'C': [('D', 5), ('E', 5), ('B', 3)],
# # #     'D': [('E', 8), ('C', 1), ('B', 2)],
# # #     'E': [('I', 5), ('J', 5), ('C', 5), ('D', 8)],
# # #     'F': [('A', 3), ('G', 1), ('H', 7)],
# # #     'G': [('F', 1), ('I', 3)],
# # #     'H': [('F', 7), ('I', 2)],
# # #     'I': [('G', 3), ('H', 2), ('E', 5), ('J', 3)],
# # #     'J': [('I', 3), ('E', 5)],
# # # }

# # # start_node = 'A'
# # # destination_node = 'J'

# # # path = uniform_cost_search(graph, start_node, destination_node)

# # # if path is None:
# # #     print('No path found from {} to {}.'.format(start_node, destination_node))
# # # else:
# # #     print('The shortest path from {} to {} is:'.format(start_node, destination_node))
# # #     print(path)
