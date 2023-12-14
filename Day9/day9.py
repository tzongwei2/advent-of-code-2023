
def f(n):

    if all(item == 0 for item in n):
        return 0
    
    else:
        temp = []
        for i in range(len(n)-1):
            temp.append(n[i+1]-n[i])
            
        return temp[-1] + f(temp)
    
def part1(lines):
    sum = 0
    for l in lines:
        l = l.split()
        l = [int(i) for i in l]
        sum += (f(l) + l[-1])
    print(sum)


def part2(lines):
    sum = 0
    for l in lines:
        l = l.split()
        l = [int(i) for i in l]
        l.reverse()
        sum += (f(l) + l[-1])
    print(sum)


if __name__ == "__main__": 

    file_path = "./day9/input.txt"

    with open(file_path, 'r') as file:
        lines = file.read()
    lines = lines.split("\n")
    
    part1(lines)
    part2(lines)
   
