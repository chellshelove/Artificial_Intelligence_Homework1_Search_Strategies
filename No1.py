from collections import deque

def find_start_and_goal(maze):
    start, goal = None, None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "G":
                goal = (i, j)
    return start, goal

def solve_maze(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] in ['0', 'G']

    def get_neighbors(x, y):
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [(nx, ny) for nx, ny in neighbors if is_valid(nx, ny)]

    start, goal = find_start_and_goal(maze)

    if start is None or goal is None:
        return "Start or goal not found in the maze."

    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for (nx, ny) in get_neighbors(x, y):
            if (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return "No path found."

def print_maze_with_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) in path:
                if (i, j) == path[-1]:
                    print("G", end=" ")
                else:
                    print("*", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

maze = [
    ["S", "1", "0", "0", "0", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "G", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0"]
]

path = solve_maze(maze)

if isinstance(path, list):
    print_maze_with_path(maze, path)
else:
    print(path)