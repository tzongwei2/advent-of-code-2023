if __name__ == "__main__": 

    file_path = "./day11/input.txt"
    matrix = []

    with open(file_path, 'r') as file:
        input = file.read().splitlines()

        galaxies = []

        for row, line in enumerate(input):
            for col, c in enumerate(line):
                if c == "#":
                    galaxies.append((row, col))

    emptyrows = [i for i, row in enumerate(input) if '#' not in row]
    emptycols = [col for col in range(len(input[0])) if all(row[col] != '#' for row in input)]
       
    sum1 = 0

    for i in range(len(galaxies)):
        for r in range(i+1,len(galaxies)):
             
             x_lower_limit = min(galaxies[i][0],galaxies[r][0])
             x_upper_limit = max(galaxies[i][0],galaxies[r][0])
             xoffset = sum(x_lower_limit < n < x_upper_limit for n in emptyrows)
      
             y_lower_limit = min(galaxies[i][1],galaxies[r][1])
             y_upper_limit = max(galaxies[i][1],galaxies[r][1])
             yoffset = sum(y_lower_limit < n < y_upper_limit for n in emptycols)

             sum1+= abs(galaxies[r][0]-galaxies[i][0]) + abs(galaxies[r][1]-galaxies[i][1]) + xoffset*999999 + yoffset*999999 #remove the 9999999 for part 1

    print(sum1)

    