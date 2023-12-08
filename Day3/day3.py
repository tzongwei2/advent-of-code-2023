import numpy as np


def getnumber(array, index, row,visited): #spread left and right to get number
   
    # lhs
    left_index = index
    while left_index >= 0 and array[left_index].isdigit():
        left_index -= 1
        visited.add((row, left_index))

    # rhs
    right_index = index
    while right_index < len(array) and array[right_index].isdigit():
        right_index += 1
        visited.add((row, right_index))

    number = array[left_index + 1:right_index]
    number = int(''.join(map(str, number)))

    return number

def part1(mapz,rows,cols):
    symbols = {"*","@","-","+","=","/","#","$","%"}
    total =0
    visited  = set()
    for r in range(rows):
        for c in range(cols):
            if mapz[r][c] in symbols: # if symbol
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 8 direction neighbors

                for direction in directions:
                    new_row, new_col = r + direction[0], c + direction[1]
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols: # check neighbor
                        if(mapz[new_row,new_col].isdigit() and (new_row, new_col) not in visited ):
                            visited.add((new_row, new_col))
                            total += getnumber(mapz[new_row],new_col,new_row,visited)
    print(total)

## part 2 
def part2(mapz,rows,cols):
    symbols = {"*"}
    visited  = set()
    total =0
    for r in range(rows):
        for c in range(cols):
            if mapz[r][c] in symbols: # if symbol
                neighbors = [] # get the gear parts
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 8 direction neighbors

                for direction in directions:
                    new_row, new_col = r + direction[0], c + direction[1]
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols: # check neighbor
                        if(mapz[new_row,new_col].isdigit() and (new_row, new_col) not in visited ):
                            visited.add((new_row, new_col))
                            # total += getnumber(mapz[new_row],new_col,new_row)
                            neighbors.append(getnumber(mapz[new_row],new_col,new_row,visited))
                
                if(len(neighbors)==2):
                    total+=(neighbors[0]*neighbors[1])

    print(total)
                       
if __name__ == "__main__": 

    file_path = "./day3/map.txt"
    mapz = [] #2d matrix
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.split()[0])
            mapz.append(row)

    mapz = np.array(mapz)
    rows,cols = mapz.shape

    part1(mapz,rows,cols)
    part2(mapz,rows,cols)
            
     
   
   