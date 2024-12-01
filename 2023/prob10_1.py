from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms

display = Display()

f = open('data10.txt', 'r')

LEFT_CONNECTIONS = ['-', '7', 'J']
RIGHT_CONNECTIONS = ['-', 'F', 'L']
UP_CONNECTIONS = ['|', 'J', 'L']
DOWN_CONNECTIONS = ['|', '7', 'F']

group_sizes = []
last_line = None
last_groups = None
animal_group = None
for l in f:
    line = '.'+l.strip()+'.'
    if last_line == None:
        last_line = '.'*len(line)
        last_groups = [-1]*len(line)
    print(line)
    
    groups = [-1]
    for i in range(1,len(line)-1):
        c = line[i]
        cl = line[i-1]
        cu = last_line[i]
        
        if c == '.':
            groups.append(-1)
            continue
        
        connected_left = c != '.' and cl !='.' and (
            (c == 'S' or cl == 'S') and (c in LEFT_CONNECTIONS or cl in RIGHT_CONNECTIONS) or
            (c in LEFT_CONNECTIONS and cl in RIGHT_CONNECTIONS)
            )
        connected_up = c != '.' and cu !='.' and (
            (c == 'S' or cu == 'S') and (c in UP_CONNECTIONS or cu in DOWN_CONNECTIONS) or
            (c in UP_CONNECTIONS and cu in DOWN_CONNECTIONS)
            )
        
        left_group = groups[i-1]
        up_group = last_groups[i]
        
        if connected_left and connected_up and left_group != up_group:
            # clear out the left group, add to the up group
            group_sizes[up_group] += group_sizes[left_group]
            group_sizes[left_group] = 0
            
            # replace existing instances of the left group
            for j, g in enumerate(last_groups):
                if g == left_group:
                    last_groups[j] = up_group
            for j, g in enumerate(groups):
                if g == left_group:
                    groups[j] = up_group
            if animal_group == left_group:
                animal_group = up_group
            groups.append(up_group)
            group_sizes[up_group] += 1
        elif connected_up:
            groups.append(up_group)
            group_sizes[up_group] += 1
        elif connected_left:
            groups.append(left_group)
            group_sizes[left_group] += 1
        else:
            # new group
            this_group = len(group_sizes)
            groups.append(this_group)
            group_sizes.append(1)
    
        if c == 'S':
            animal_group = groups[-1]
    
    print(groups)
    print(group_sizes)
    
    last_groups = groups
    last_line = line
    
    display.fill(0)
    display.text(f"Groups: {len(list(i for i in group_sizes if i != 0))}", 0,10)
    if animal_group != None:
        display.text(f"Animal: {animal_group}", 0,20)
        display.text(f"Size: {group_sizes[animal_group]}", 0, 30)
        display.text(f"Dist: {group_sizes[animal_group]//2}", 0, 50)
    display.show()
 



