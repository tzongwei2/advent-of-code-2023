def add_adjacent_cells(adj_matrix, rows, cols, row, col, directions,start = False):
    neighbors = []
    for direction in directions:
 
        new_row, new_col = get_new_coordinates(row, col, direction)
        if check_bounds(rows, cols, new_row, new_col):
            neighbors.append((new_row,new_col))
    if not start:
        adj_matrix[row].append(neighbors)
    else:

        adj_matrix[row][col] = [] #clean the matrix for the start pos

        for item in neighbors:
            adj_matrix[row][col].append(item)



def get_new_coordinates(row, col, direction):
    if direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1
    elif direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col

def check_bounds(rows, cols, row, col):
    return 0 <= row < rows and 0 <= col < cols


def modified_dfs(adj_matrix,startindex): #this dfs checks for cycle and also keeps track of the current distance from start node
    visited = set()

    
    if startindex not in visited:
        stack = [(startindex, None)]  # (node, parent)
        distance = 0

        while stack:
            current_node, parent = stack.pop()

            if current_node in visited:
                # If the current node is already visited, and it's not the parent, a cycle exists
                if current_node != parent:
                    return distance,visited
                continue
           
            distance +=1
            visited.add(current_node)

            for neighbor in adj_matrix[current_node[0]][current_node[1]]:
                if(neighbor not in visited):
                    stack.append((neighbor, current_node))

    return -1

def part1(graph):
    rows, cols = len(graph), len(graph[0])

    #adjacency matrix containing neighbors
    adj_matrix = [[] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if graph[row][col] == ".":
                 adj_matrix[row].append([])

            if graph[row][col] == "-":
                add_adjacent_cells(adj_matrix, rows, cols, row, col, ["left", "right"])

            elif graph[row][col] == "|":
                add_adjacent_cells(adj_matrix, rows, cols, row, col, ["up", "down"])

            elif graph[row][col] in ["L"]:
                add_adjacent_cells(adj_matrix, rows, cols, row, col, ["up", "right"])

            elif graph[row][col] in ["J"]:
                add_adjacent_cells(adj_matrix, rows, cols, row, col, ["up", "left"])

            elif graph[row][col] in ["7"]:
                add_adjacent_cells(adj_matrix, rows, cols, row, col, ["down", "left"])

            elif graph[row][col] in ["F"]:
                add_adjacent_cells(adj_matrix, rows, cols, row, col, ["down", "right"])

            elif graph[row][col] in ["S"]:
                adj_matrix[row].append([])
                startindex = (row,col)
    

    for pipe in ["L","|","-","J","7","F"]:
        graph[startindex[0]][startindex[1]] = pipe
        add_adjacent_cells(adj_matrix, rows, cols, startindex[0], startindex[1], ["down", "right"],True)
        distance,visited = modified_dfs(adj_matrix,startindex)
        print(int(distance/2))
        break

    # Part 2 I will use point in polygon method. to determine if a point in polygon, shoot a ray to the left. if 3 intersection, it is inside, if 4, it is outside! 
    # I actually have a github gist on this method I did some time ago.

    points = 0
   
    for row in range(1,rows -1):
        for col in range(1,cols -1 ):
           
            if(row,col) in visited:
                continue

            ray_count = 0
            x2,y2 = row,col

            while x2 < rows and y2 < cols:
             
                if (x2,y2) in visited and graph[x2][y2] not in ["L","7"]:
                    ray_count += 1

                x2 += 1
                y2 += 1
                
            if ray_count % 2 == 1:
                points += 1

    print(points)
              

    
    

                    


if __name__ == "__main__": 

    file_path = "./day10/input.txt"

    with open(file_path, 'r') as file:
        lines = file.read()
    lines = lines.split("\n")
    graph = []
    for line in lines:
        line = list(line)
        graph.append(line)
    
    part1(graph)
    
   