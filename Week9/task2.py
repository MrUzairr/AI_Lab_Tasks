import heapq

def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def print_grid_with_path(grid, path):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == path[0]:
                print('S', end=' ')
            elif (i, j) == path[-1]:
                print('G', end=' ')
            elif (i, j) in path:
                print('.', end=' ')
            else:
                print(grid[i][j], end=' ')
        print()

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = [(0, start)]
    closed_set = set()
    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        closed_set.add(current)

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + i, current[1] + j

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] != 'X':
                tentative_g_score = g_score[current] + 1

                if neighbor not in closed_set or tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))



    return None  # No path found

# Example usage
grid = [
    ['S', '.', '.', 'X', 'X'],
    ['.', 'X', '.', '.', '.'],
    ['.', 'X', 'X', '.', 'X'],
    ['.', '.', '.', '.', '.'],
    ['X', '.', 'X', 'X', 'G']
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)

if path:
    print("Shortest path:", path)
    print("Number of steps:", len(path) - 1)
    for step in path:
        print_grid_with_path(grid, [step])
        print()
else:
    print("No path found.")

# class Node:
#     def __init__(self, x, y, g, h, parent=None):
#         self.x = x
#         self.y = y
#         self.g = g  # cost of the path from the start node to this node
#         self.h = h  # estimated cost of reaching the goal node from this node
#         self.f = g + h  # total cost of the path to this node
#         self.parent = parent

# def a_star_search(start_node, goal_node, grid, max_iterations=10000):
#     """Finds the shortest path from the start node to the goal node on the grid, avoiding obstacles."""

#     open_list = []  # priority queue of nodes to be explored
#     closed_set = set()  # set of explored nodes

#     open_list.append(start_node)

#     iterations = 0

#     while open_list and iterations < max_iterations:
#         node = min(open_list, key=lambda x: x.f)
#         open_list.remove(node)

#         if node == goal_node:
#             return reconstruct_path(node)

#         closed_set.add(node)

#         for neighbor in get_neighbors(node, grid):
#             if neighbor not in closed_set:
#                 new_g = node.g + 1
#                 new_h = manhattan_distance(neighbor, goal_node)
#                 new_f = new_g + new_h

#                 if neighbor not in open_list or new_f < neighbor.f:
#                     neighbor.g = new_g
#                     neighbor.h = new_h
#                     neighbor.f = new_f
#                     neighbor.parent = node

#                     if neighbor not in open_list:
#                         open_list.append(neighbor)

#         iterations += 1

#     return None
# def reconstruct_path(node):
#     """Reconstructs the path from the given node to the start node."""

#     path = []
#     while node:
#         path.append(node)
#         node = node.parent

#     path.reverse()
#     return path

# def get_neighbors(node, grid):
#     """Returns a list of all the neighbors of the given node on the grid."""

#     neighbors = []

#     for x in range(-1, 2):
#         for y in range(-1, 2):
#             new_x = node.x + x
#             new_y = node.y + y

#             if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#                 if grid[new_y][new_x] != "X":
#                     neighbors.append(Node(new_x, new_y, node.g + 1, manhattan_distance(Node(new_x, new_y, 0, 0), goal_node)))

#     return neighbors

# # ... (rest of the code remains the same)
# def print_grid(grid, path):
#     """Prints the grid with the shortest path marked with asterisks."""

#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if any(node.x == x and node.y == y for node in path):
#                 print("*", end="")
#             else:
#                 print(grid[y][x], end="")
#         print()


# def manhattan_distance(node1, node2):
#     """Calculates the Manhattan distance between the two given nodes."""

#     return abs(node1.x - node2.x) + abs(node1.y - node2.y)

# grid = [['S', '.', '.', 'X', 'X'],
#         ['.', 'X', '.', '.', '.'],
#         ['.', 'X', 'X', '.', 'X'],
#         ['.', '.', '.', '.', '.'],
#         ['X', '.', 'X', 'X', 'G']]

# start_node = Node(0, 0, 0, manhattan_distance(Node(0, 0, 0, 0), Node(4, 4, 0, 0)))
# goal_node = Node(4, 4, 0, manhattan_distance(Node(4, 4, 0, 0), Node(4, 4, 0, 0)))

# path = a_star_search(start_node, goal_node, grid)

# if path:
#     print_grid(grid, path)
# else:
#     print("Goal is unreachable.")


# class Node:
#     def __init__(self, x, y, g, h, parent=None):
#         self.x = x
#         self.y = y
#         self.g = g  # cost of the path from the start node to this node
#         self.h = h  # estimated cost of reaching the goal node from this node
#         self.f = g + h  # total cost of the path to this node
#         self.parent = parent

# def a_star_search(start_node, goal_node, grid):
#     """Finds the shortest path from the start node to the goal node on the grid, avoiding obstacles."""

#     open_list = []  # priority queue of nodes to be explored
#     closed_set = set()  # set of explored nodes

#     open_list.append(start_node)

#     while open_list:
#         node = min(open_list, key=lambda x: x.f)
#         open_list.remove(node)

#         if node == goal_node:
#             return reconstruct_path(node)

#         closed_set.add(node)

#         for neighbor in get_neighbors(node, grid):
#             if neighbor not in closed_set:
#                 new_g = node.g + 1
#                 new_h = manhattan_distance(neighbor, goal_node)
#                 new_f = new_g + new_h

#                 if neighbor not in open_list or new_f < neighbor.f:
#                     neighbor.g = new_g
#                     neighbor.h = new_h
#                     neighbor.f = new_f
#                     neighbor.parent = node

#                     if neighbor not in open_list:
#                         open_list.append(neighbor)

#     return None

# # ... (rest of the code remains the same)

# def get_neighbors(node, grid):
#     """Returns a list of all the neighbors of the given node on the grid."""

#     neighbors = []

#     for x in range(-1, 2):
#         for y in range(-1, 2):
#             new_x = node.x + x
#             new_y = node.y + y

#             if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#                 if grid[new_y][new_x] != "X":
#                     neighbors.append(Node(new_x, new_y, node.g + 1, manhattan_distance(Node(new_x, new_y, 0, 0), goal_node)))

#     return neighbors
# def manhattan_distance(node1, node2):
#     """Calculates the Manhattan distance between the two given nodes."""

#     return abs(node1.x - node2.x) + abs(node1.y - node2.y)

# def print_grid(grid, path):
#     """Prints the grid with the shortest path marked with asterisks."""

#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if any(node.x == x and node.y == y for node in path):
#                 print("*", end="")
#             else:
#                 print(grid[y][x], end="")
#         print()

# grid = [['S', '.', '.', 'X', 'X'],
#         ['.', 'X', '.', '.', '.'],
#         ['.', 'X', 'X', '.', 'X'],
#         ['.', '.', '.', '.', '.'],
#         ['X', '.', 'X', 'X', 'G']]

# start_node = Node(0, 0, 0, manhattan_distance(Node(0, 0, 0, 0), Node(4, 4, 0, 0)))
# goal_node = Node(4, 4, 0, manhattan_distance(Node(4, 4, 0, 0), Node(4, 4, 0, 0)))

# path = a_star_search(start_node, goal_node, grid)

# print_grid(grid, path)



# class Node:
#     def __init__(self, x, y, g, h, parent=None):
#         self.x = x
#         self.y = y
#         self.g = g  # cost of the path from the start node to this node
#         self.h = h  # estimated cost of reaching the goal node from this node
#         self.f = g + h  # total cost of the path to this node
#         self.parent = parent

# def a_star_search(start_node, goal_node, grid):
#     """Finds the shortest path from the start node to the goal node on the grid, avoiding obstacles."""

#     open_list = []  # priority queue of nodes to be explored
#     closed_list = set()  # set of explored nodes

#     open_list.append(start_node)

#     while open_list:
#         node = open_list.pop(0)

#         if node == goal_node:
#             return reconstruct_path(node)

#         closed_list.add(node)

#         for neighbor in get_neighbors(node, grid):
#             if neighbor not in closed_list:
#                 new_g = node.g + 1
#                 new_h = manhattan_distance(neighbor, goal_node)
#                 new_f = new_g + new_h

#                 if neighbor not in open_list or new_f < neighbor.f:
#                     neighbor.g = new_g
#                     neighbor.h = new_h
#                     neighbor.f = new_f
#                     neighbor.parent = node

#                     open_list.append(neighbor)

#     return None

# def reconstruct_path(node):
#     """Reconstructs the path from the given node to the start node."""

#     path = []
#     while node:
#         path.append(node)
#         node = node.parent

#     path.reverse()
#     return path

# def get_neighbors(node, grid):
#     """Returns a list of all the neighbors of the given node on the grid."""

#     neighbors = []

#     for x in range(-1, 2):
#         for y in range(-1, 2):
#             new_x = node.x + x
#             new_y = node.y + y

#             if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#                 if grid[new_y][new_x] != "X":
#                     neighbors.append(Node(new_x, new_y, node.g + 1, manhattan_distance(Node(new_x, new_y, 0, 0), goal_node)))

#     return neighbors

# def manhattan_distance(node1, node2):
#     """Calculates the Manhattan distance between the two given nodes."""

#     return abs(node1.x - node2.x) + abs(node1.y - node2.y)

# def print_grid(grid, path):
#   """Prints the grid with the shortest path marked with asterisks."""

#   for y in range(len(grid)):
#     for x in range(len(grid[0])):
#       if node in path:
#         print("*", end="")
#       else:
#         print(grid[y][x], end="")
#     print()

# grid = [['S', '.', '.', 'X', 'X'],
#           ['.', 'X', '.', '.', '.'],
#           ['.', 'X', 'X', '.', 'X'],
#           ['.', '.', '.', '.', '.'],
#           ['X', '.', 'X', 'X', 'G']]

# start_node = Node(0, 0, 0, manhattan_distance(Node(0, 0, 0, 0), Node(4, 4, 0, 0)))
# goal_node = Node(4, 4, 0, manhattan_distance(Node(4, 4, 0, 0), Node(4, 4, 0, 0)))

# path = a_star_search(start_node, goal_node, grid)

# print_grid(grid, path)


# class Node:
#     def __init__(self, x, y, g, h, parent=None):
#         self.x = x
#         self.y = y
#         self.g = g  # cost of the path from the start node to this node
#         self.h = h  # estimated cost of reaching the goal node from this node
#         self.f = g + h  # total cost of the path to this node
#         self.parent = parent

# def a_star_search(start_node, goal_node, grid):
#     """Finds the shortest path from the start node to the goal node on the grid, avoiding obstacles."""

#     open_list = []  # priority queue of nodes to be explored
#     closed_list = []  # set of explored nodes

#     open_list.append(start_node)

#     while open_list:
#         node = open_list.pop(0)

#         if node == goal_node:
#             return reconstruct_path(node)

#         closed_list.add(node)

#         for neighbor in get_neighbors(node, grid):
#             if neighbor not in closed_list:
#                 new_g = node.g + 1
#                 new_h = manhattan_distance(neighbor, goal_node)
#                 new_f = new_g + new_h

#                 if neighbor not in open_list or new_f < neighbor.f:
#                     neighbor.g = new_g
#                     neighbor.h = new_h
#                     neighbor.f = new_f
#                     neighbor.parent = node

#                     open_list.append(neighbor)

#     return None

# def reconstruct_path(node):
#     """Reconstructs the path from the given node to the start node."""

#     path = []
#     while node:
#         path.append(node)
#         node = node.parent

#     path.reverse()
#     return path

# def get_neighbors(node, grid):
#     """Returns a list of all the neighbors of the given node on the grid."""

#     neighbors = []

#     for x in range(-1, 2):
#         for y in range(-1, 2):
#             new_x = node.x + x
#             new_y = node.y + y

#             if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#                 if grid[new_y][new_x] != "X":
#                     neighbors.append(Node(new_x, new_y, node.g + 1, manhattan_distance(Node(new_x, new_y, 0, 0), goal_node)))

#     return neighbors

# def manhattan_distance(node1, node2):
#     """Calculates the Manhattan distance between the two given nodes."""

#     return abs(node1.x - node2.x) + abs(node1.y - node2.y)

# def print_grid(grid, path):
#   """Prints the grid with the shortest path marked with asterisks."""

#   for y in range(len(grid)):
#     for x in range(len(grid[0])):
#       if node in path:
#         print("*", end="")
#       else:
#         print(grid[y][x], end="")
#     print()

# grid = [['S', '.', '.', 'X', 'X'],
#          ['.', 'X', '.', '.', '.'],
#          ['.', 'X', 'X', '.', 'X'],
#          ['.', '.', '.', '.', '.'],
#          ['X', '.', 'X', 'X', 'G']]

# start_node = Node(0, 0, 0, manhattan_distance(Node(0, 0, 0, 0), Node(4, 4, 0, 0)))
# goal_node = Node(4, 4, 0, manhattan_distance(Node(4, 4, 0, 0), Node(4, 4, 0, 0)))

# path = a_star_search(start_node, goal_node, grid)

# print_grid(grid, path)

# import heapq

# def astar(grid, start, goal):
#     rows, cols = len(grid), len(grid[0])
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Possible movements: down, right, up, left

#     def heuristic(node):
#         return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

#     priority_queue = [(0, start)]
#     visited = set()

#     while priority_queue:
#         cost, current = heapq.heappop(priority_queue)

#         if current == goal:
#             return cost

#         if current in visited:
#             continue

#         visited.add(current)

#         for direction in directions:
#             next_row, next_col = current[0] + direction[0], current[1] + direction[1]

#             if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] != 'X':
#                 new_cost = cost + 1
#                 heapq.heappush(priority_queue, (new_cost + heuristic((next_row, next_col)), (next_row, next_col)))

#     return float('inf')  # No path found

# # Example grid
# grid = [
#     ['S', '.', '.', 'X', 'X'],
#     ['.', 'X', '.', '.', '.'],
#     ['.', 'X', 'X', '.', 'X'],
#     ['.', '.', '.', '.', '.'],
#     ['X', '.', 'X', 'X', 'G']
# ]

# start_point = None
# goal_point = None

# # Find start and goal points
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == 'S':
#             start_point = (i, j)
#         elif grid[i][j] == 'G':
#             goal_point = (i, j)

# if start_point and goal_point:
#     shortest_path_length = astar(grid, start_point, goal_point)
#     if shortest_path_length != float('inf'):
#         print(f"Shortest path length: {shortest_path_length}")
#     else:
#         print("No valid path found.")
# else:
#     print("Start or goal point not found.")




# import heapq

# # Define grid constants
# START = 'S'
# GOAL = 'G'
# OBSTACLE = 'X'
# OPEN_SPACE = '.'

# # Define movements (up, down, left, right, and diagonals)
# MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# def heuristic(node, goal):
#     # Calculate the Manhattan distance as the heuristic
#     return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# def a_star(grid, start, goal):
#     # Define a priority queue for the open set
#     open_set = []
#     heapq.heappush(open_set, (0, start))

#     # Create dictionaries to track costs and parent nodes
#     g_score = {start: 0}
#     parent = {start: None}

#     while open_set:
#         _, current = heapq.heappop(open_set)

#         if current == goal:
#             # Reconstruct the path
#             path = []
#             while current:
#                 path.append(current)
#                 current = parent[current]
#             path.reverse()
#             return path

#         for move in MOVES:
#             neighbor = (current[0] + move[0], current[1] + move[1])

#             if neighbor[0] < 0 or neighbor[0] >= len(grid) or neighbor[1] < 0 or neighbor[1] >= len(grid[0]) or grid[neighbor[0]][neighbor[1]] == OBSTACLE:
#                 continue

#             tentative_g_score = g_score[current] + 1

#             if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                 g_score[neighbor] = tentative_g_score
#                 f_score = tentative_g_score + heuristic(neighbor, goal)
#                 heapq.heappush(open_set, (f_score, neighbor))
#                 parent[neighbor] = current

#     return None  # No path found

# # Example usage
# grid = [
#     "S..X.....",
#     ".X.......",
#     ".X.X.....",
#     "....X....",
#     "..X..X...",
#     "...X...X.",
#     "......X..",
#     "........G"
# ]

# # Convert the grid to a list of lists
# grid = [list(row) for row in grid]
# print(grid)

# start_pos = (0, 0)
# goal_pos = len(grid)
