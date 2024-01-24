from collections import deque

def breadth_first_search(graph, start, goal):
    queue = deque()
    queue.append([start])

    visited = set()

    while queue:
        path = queue.popleft()
        print(path)
        current_node = path[-1]

        if current_node == goal:
            return path 

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                new_path = list(path) 
                new_path.append(neighbor)
                queue.append(new_path)

    return None 

def depth_first_search(graph, start, goal):
    def dfs_util(node, path):
        if node == goal:
            return path 
        
        visited.add(node)
        print("-->{} ".format(graph[node]))
        for neighbor in graph[node]:
            print('neighbor: {}'.format(neighbor))
            if neighbor not in visited:
                new_path = path + [neighbor]
                print('new_path: {}'.format(new_path))
                result = dfs_util(neighbor, new_path)
                if result:
                    return result

        return None 
    
    visited = set()
    start_path = [start]
    result_path = dfs_util(start, start_path)

    return result_path

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }

    start_node = 'A'
    goal_node = 'G'

    result_path = depth_first_search(graph, start_node, goal_node)

    if result_path:
        print(f"DFS Path from {start_node} to {goal_node}: {result_path}")
    else:
        print(f"DFS No path found from {start_node} to {goal_node}.")

    result_path1 = breadth_first_search(graph, start_node, goal_node)

    if result_path1:
        print(f"BFS Path from {start_node} to {goal_node}: {result_path1}")
    else:
        print(f"BFS No path found from {start_node} to {goal_node}.")