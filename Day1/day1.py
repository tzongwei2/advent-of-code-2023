def part1(lines):
    totalsum = 0
    for code in lines:
        n1 = 0
        n2 = 0
        for x in range(len(code)):

            if(code[x].isdigit() and n1 == 0):
                n1 = code[x]
        
            temp = code[len(code)-x-1]
            if(temp.isdigit() and n2 == 0):
                n2 = temp

        number = n1+n2
        totalsum+= int(number)

    print(totalsum)

## Part 2 
def part2(lines):
    totalsum = 0
    numbersdict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }

    totalsum = 0

    for code in lines:
        numbers = []
        for x in range(len(code)):
            if code[x].isdigit():
                numbers.append(str(code[x]))
            else:
                string = ""
                for i in range(0, min(6, len(code) - 1 - x + 1)):
                    string += code[x + i]
                    if string in numbersdict:
                        numbers.append(numbersdict[string])
                        string = ""
                        break

        cursum = numbers[0] + numbers[-1]
        totalsum += int(cursum)

    print(totalsum)

if __name__ == "__main__": 
    file_path = "./Day1/calibrationdoc.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    part1(lines)
    part2(lines)
