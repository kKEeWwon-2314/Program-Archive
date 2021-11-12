import sys
sys.setrecursionlimit(10000)
"""
0 0 1 0 0 ← (0, 4)
0 0 0 0 0 
0 0 0 1 0 
1 1 0 1 1 
0 0 0 0 0 ← (4, 4)
"""
def DFS_support(maze, start, end, visited):
    # Head of recursion
    if (maze[start[0]][start[1]] == 1):
        return False
    if (visited[start[0]][start[1]]):
        return False
    if (start[0] == end[0] and start[1] == end[1]):
        return True

    visited[start[0]][start[1]] = True

    # Right
    if (start[1] < len(maze[0]) - 1):
        right = (start[0], start[1] + 1)
        if (DFS_support(maze, right, end, visited)):
            return True

    # Left
    if (start[1] > 0):
        left = (start[0], start[1] - 1)
        if (DFS_support(maze, left, end, visited)):
            return True

    # Up (Counter-intuitive, the maze is backwards)
    if (start[0] > 0):
        up = (start[0] - 1, start[1])
        if (DFS_support(maze, up, end, visited)):
            return True 

    # Down (Counter-intuitive, the maze is backwards)
    if (start[0] < len(maze[0]) - 1):
        down = (start[0] + 1, start[1])
        if (DFS_support(maze, down, end, visited)):
            return True
    
    # If none of the above statements comply, we will return FALSE
    return False

def DFS(maze, start, end):
    visited = [[False] * len(maze[0]) for i in range(len(maze))]
    return DFS_support(maze, start, end, visited)

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

start_coords = list(map(int, input().split()))
end_coords = list(map(int, input().split()))

print(DFS(maze, start_coords, end_coords))
