import re 


def part1(time,distance):
    ways = 1
    for i in range(len(time)):
        tobeat = int(distance[i])
        possible_times = [x + 1 for x in range(int(time[i])-1)]
        l =0
        r = len(possible_times) -1 
        while(l<=r):

            l_distance = possible_times[l]*(int(time[i])-possible_times[l])
            if(l_distance <= tobeat):
                l+=1

            r_distance = possible_times[r]*(int(time[i]) -possible_times[r])
            if(r_distance <= tobeat):
                r-=1
          
            if(l_distance >= tobeat and r_distance >= tobeat):
                break

        ways*=((r-l)+1)
    print(ways)


def part2(time,distance):
    ways = 1
    time = "".join(time)
    distance = "".join(distance)
    tobeat = int(distance)
   
    possible_times = [x + 1 for x in range(int(time)-1)]
    l =0
    r = len(possible_times) -1 
    while(l<=r):

        l_distance = possible_times[l]*(int(time)-possible_times[l])
        if(l_distance <= tobeat):
            l+=1

        r_distance = possible_times[r]*(int(time) -possible_times[r])
        if(r_distance <= tobeat):
            r-=1
        
        if(l_distance >= tobeat and r_distance >= tobeat):
            break

    ways*=((r-l)+1)
    print(ways)

     
            

            







if __name__ == "__main__": 
    file_path = "./day6/input.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        time=  re.findall(r'\b\d+\b', lines[0])
        distance=  re.findall(r'\b\d+\b', lines[1])
    
    part1(time,distance)
    part2(time,distance)