from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
from array import array

display = Display()

f = open('data10.txt', 'r')

LEFT_CONNECTIONS = ['-', '7', 'J']
RIGHT_CONNECTIONS = ['-', 'F', 'L']
UP_CONNECTIONS = ['|', 'J', 'L']
DOWN_CONNECTIONS = ['|', '7', 'F']

group_count = 0
inner_area = array('h', [0]*6000)
outer_area = array('h', [0]*6000)
up_inside = array('B', [False]*6000)
down_inside = array('B', [False]*6000)

last_line = None
last_groups = None
animal_group = None
y = 0
for l in f:
    line = '.'+l.strip()+'.'
    if last_line == None:
        last_line = '.'*len(line)
        last_groups = [-1]*len(line)
    #print("")
    print(f"{y}: {line}")
    
    groups = [-1]
    for i in range(len(up_inside)):
        up_inside[i] = False
        down_inside[i] = False
    
    for i in range(1,len(line)-1):
        c = line[i]
        cl = line[i-1]
        cr = line[i+1]
        cu = last_line[i]
        
        if c == '.':
            groups.append(-1)
            continue
        
        connected_left = c != '.' and cl !='.' and (
            (c == 'S' or cl == 'S') and (c in LEFT_CONNECTIONS or cl in RIGHT_CONNECTIONS) or
            (c in LEFT_CONNECTIONS and cl in RIGHT_CONNECTIONS)
            )
        connected_right = c != '.' and cr !='.' and (
            (c == 'S' or cr == 'S') and (c in RIGHT_CONNECTIONS or cr in LEFT_CONNECTIONS) or
            (c in RIGHT_CONNECTIONS and cr in LEFT_CONNECTIONS)
            )
        connected_up = c != '.' and cu !='.' and (
            (c == 'S' or cu == 'S') and (c in UP_CONNECTIONS or cu in DOWN_CONNECTIONS) or
            (c in UP_CONNECTIONS and cu in DOWN_CONNECTIONS)
            )
        
        left_group = groups[i-1]
        up_group = last_groups[i]
        
        if connected_left and connected_up and left_group != up_group:
            
            if not up_inside[left_group] and up_inside[up_group]:
                new_ia = outer_area[left_group] + inner_area[up_group]
                new_oa = inner_area[left_group] + outer_area[up_group]
                down_inside[up_group] = not down_inside[left_group]
            elif up_inside[left_group] and not up_inside[up_group]:
                new_ia = inner_area[left_group] + outer_area[up_group]
                new_oa = outer_area[left_group] + inner_area[up_group]
                up_inside[up_group] = True
                down_inside[up_group] = down_inside[left_group]
            elif not up_inside[left_group] and not up_inside[up_group]:
                new_ia = inner_area[left_group] + inner_area[up_group]
                new_oa = outer_area[left_group] + outer_area[up_group]
                down_inside[up_group] = down_inside[left_group]
            else:
                # inside both can't happen for a closed group, I think
                pass
            #print(f"{left_group}+{up_group} at {i} ({up_inside[left_group]} {up_inside[up_group]}): {inner_area[left_group]} {outer_area[left_group]} / {inner_area[up_group]} {outer_area[up_group]} -> {new_ia} {new_oa}")
            inner_area[up_group] = new_ia
            outer_area[up_group] = new_oa
            inner_area[left_group] = 0
            outer_area[left_group] = 0
            
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
        elif connected_up:
            groups.append(up_group)
        elif connected_left:
            groups.append(left_group)
        else:
            # new group
            this_group = group_count
            groups.append(this_group)
            group_count += 1
            up_inside[group_count] = False
            down_inside[group_count] = False
            inner_area[group_count] = 0
            outer_area[group_count] = 0
    
        if c == 'S':
            animal_group = groups[-1]
    
        # work out the areas
        connected_down = (connected_left + connected_right + connected_up < 2)
        this_group = groups[i]
            
        up_in = up_inside[this_group]
        next_up_in = up_in
        down_in = down_inside[this_group]
        next_down_in = down_in
        if connected_up:
            next_up_in = not up_in # switching sides
            up_in = False # up is blocked, so it can't be "inside"
        if connected_down:
            next_down_in = not down_in
            down_in = False
        
        if connected_right or connected_left: # there will be some areas to adjust
            if down_in and not up_in:
                inner_area[this_group] -= y + 1
            if up_in and not down_in:
                inner_area[this_group] += y
            if not down_in and not connected_down:
                outer_area[this_group] -= y + 1
            if not up_in and not connected_up:
                outer_area[this_group] += y
        
        up_inside[this_group] = next_up_in
        down_inside[this_group] = next_down_in
    
    #print(groups)
    #print(f"in: {inner_area}")
    #print(f"out: {outer_area}")
    
    last_groups = groups
    last_line = line
    y += 1
    
    display.fill(0)
    display.text(f"Groups: {group_count}", 0,10)
    if animal_group != None:
        display.text(f"Animal: {animal_group}", 0,20)
        display.text(f"Area: {inner_area[animal_group]}", 0, 50)
    display.show()
 



