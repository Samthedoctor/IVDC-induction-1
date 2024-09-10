from collections import deque

def bfs_grid(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)] 
    queue = deque([start])
    visited = set([start])
    predecessor = {start: None} 

    while queue:
        current = queue.popleft()
        current_row, current_col = current

        if current == target:
           
            path = []
            while current is not None:
                path.append(current)
                current = predecessor[current]
            return path[::-1]  

        for direction in directions:
            new_row, new_col = current_row + direction[0], current_col + direction[1]
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                grid[new_row][new_col] == 0 and (new_row, new_col) not in visited):
                next_cell = (new_row, new_col)
                queue.append(next_cell)
                visited.add(next_cell)
                predecessor[next_cell] = current  
    return [] 


grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
target = (4, 4)


path = bfs_grid(grid, start, target)
print(f"The path is: {path}")