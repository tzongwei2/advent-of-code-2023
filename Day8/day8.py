import math

def part1(moves, mapping):
    start = 'AAA'
    steps = 0
    cur = start
    while(cur != 'ZZZ'):
        for move in moves:
            if cur == 'ZZZ':
                break
            if move =='R':
                cur = mapping[cur][1]
            
            if move =='L':
                cur = mapping[cur][0]

            steps+=1
    print(steps)


def part2(moves, mapping):
    starts = [key for key in mapping.keys() if key[-1]=="A"]
    stepstaken = []
    for start in starts:
        steps = 0
        cur = start
        while(cur[-1] != 'Z'):
            for move in moves:
            
                if cur[-1] == 'Z':
                    break
                if move =='R':
                    cur = mapping[cur][1]
                
                if move =='L':
                    cur = mapping[cur][0]

                steps+=1
        stepstaken.append(steps)
    lcm = math.lcm(*stepstaken)
    print(lcm)





if __name__ == "__main__": 

    file_path = "./day8/input.txt"
    map_dict = {}

    with open(file_path, 'r') as file:
        lines = file.read()
    moves, mapping = lines.strip().split("\n\n")
    mapping = mapping.split("\n")

    for path in mapping:
        key,value = path.split("=")
        value = value[2:-1].strip()
        values = value.split(", ")
        map_dict[key[:-1]] = tuple(values)

    part1(moves,map_dict)
    part2(moves, map_dict)

 

 





   
    