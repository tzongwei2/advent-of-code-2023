

def part1(lines):
    profit = 0
    for line in lines:
        card_list = line.split(":")
        winning_nums, my_nums = card_list[1].split("|")
        #split into a set
        my_nums = my_nums.split()
        my_nums = set(map(int, my_nums))
        winning_nums = winning_nums.split()
        winning_nums = set(map(int, winning_nums))

        common_items = my_nums.intersection(winning_nums)
     
        if len(common_items) > 0:
            profit += 2**(len(common_items)-1)

    print(profit)



def part2(lines):
    cards = [1]*len(lines) # 1 of each card initially
    i = 0 # index

    for line in lines:
        card_list = line.split(":")
        winning_nums, my_nums = card_list[1].split("|")
        
        #split into a set
        my_nums = my_nums.split()
        my_nums = set(map(int, my_nums))
        winning_nums = winning_nums.split()
        winning_nums = set(map(int, winning_nums))

        temp = i
        for num in my_nums:
            if num in winning_nums:    
                temp += 1
                cards[temp] += cards[i]
        i+=1
  
    print(sum(cards))

      

        

    


        

if __name__ == "__main__": 
    file_path = "./day4/input.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    part1(lines)
    part2(lines)
    