import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return self.depth < other.depth

class SlidingPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.size = 3
        self.moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # Possible moves: Left, Up, Right, Down

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def generate_children(self, node):
        children = []
        empty_x, empty_y = node.state.index(0) // self.size, node.state.index(0) % self.size

        for dx, dy in self.moves:
            new_x, new_y = empty_x + dx, empty_y + dy
            if self.is_valid_move(new_x, new_y):
                new_state = node.state[:]
                index1 = empty_x * self.size + empty_y
                index2 = new_x * self.size + new_y
                new_state[index1], new_state[index2] = new_state[index2], new_state[index1]
                move = (dx, dy)
                child_node = PuzzleNode(new_state, parent=node, move=move, depth=node.depth + 1)
                children.append(child_node)

        return children

    def heuristic(self, state):
        h_score = 0
        for i in range(self.size):
            for j in range(self.size):
                if state[i * self.size + j] != 0:
                    target_x, target_y = (state[i * self.size + j] - 1) // self.size, (state[i * self.size + j] - 1) % self.size
                    h_score += abs(i - target_x) + abs(j - target_y)
        return h_score
    
    def build_solution(self, node):
        path = []
        while node:
            path.insert(0, node.move)
            node = node.parent
        return path

    def solve(self):
        open_list = []
        closed_set = set()
        initial_node = PuzzleNode(self.initial_state)
        heapq.heappush(open_list, initial_node)

        while open_list:
            current_node = heapq.heappop(open_list)

            if current_node.state == self.goal_state:
                return self.build_solution(current_node)

            closed_set.add(tuple(current_node.state))

            for child in self.generate_children(current_node):
                if tuple(child.state) not in closed_set:
                    child.depth += self.heuristic(child.state)
                    heapq.heappush(open_list, child)

        return None
    
    def print_puzzle(state):
        for i in range(3):
            for j in range(3):
                tile = state[i * 3 + j]
                if tile == 0:
                    print("   ", end=" ")
                else:
                    print(f" {tile} ", end=" ")
            print()

#-----------------------------------------------
initial_state = [1, 2, 3, 4, 0, 6, 7, 8, 9]
goal_state = [1, 0, 3, 6, 8, 4, 9, 2, 7]

puzzle = SlidingPuzzle(initial_state, goal_state)

SlidingPuzzle.print_puzzle(initial_state)
print("-----------")
SlidingPuzzle.print_puzzle(goal_state)

solution = puzzle.solve()

print(solution)
