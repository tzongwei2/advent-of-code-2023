# Part 1
def part1(file_path):
    totalsum = 0
    qlimit = {'red':12,"green":13,"blue":14}

    with open(file_path, 'r') as file:
        for line in file:

            sets = line.split(';') # sets represent one game
            maxq = {'red':0,"green":0,"blue":0}
            for set in sets: # set are the rounds in a game

                colon_index = set.find(':')

                if colon_index != -1: # get the game number
                    game = set[:colon_index].strip()
                    gamenumber = game.split()[1]
                    
                set = set[colon_index+1:] # filter out only the results
                
                color_quantity_pairs = [pair.strip().split() for pair in set.split(',')]

                for element in color_quantity_pairs:
                        qty,color = element
                        maxq[color] = max(maxq[color],int(qty)) 
                
            accepted = all(maxq[color] <= qlimit[color] for color in maxq)

            if(accepted):
                totalsum+=int(gamenumber)

    print(totalsum)


#part 2 
def part2(file_path):
    totalpower = 0
    with open(file_path, 'r') as file:
        for line in file:

            sets = line.split(';') # sets represent one game
            maxq = {'red':0,"green":0,"blue":0}
            for set in sets: # set are the rounds in a game

                colon_index = set.find(':')
                set = set[colon_index+1:] # filter out only the results
                
                color_quantity_pairs = [pair.strip().split() for pair in set.split(',')]

                for element in color_quantity_pairs:
                        qty,color = element
                        maxq[color] = max(maxq[color],int(qty)) 

            power = 1
            for value in maxq.values():
                power *= value

            totalpower += power

    print(totalpower)

if __name__ == "__main__": 
    file_path = "./day2/data.txt"
    part1(file_path)
    part2(file_path)