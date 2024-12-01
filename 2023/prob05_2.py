from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
import re

display = Display()

def print3line(s):
    display.text(s, 0, 0)
    display.text(s[16:], 0, 10)
    display.text(s[32:], 0, 20)

f = open('data05.txt', 'r')

seeds_line = next(f).strip()
seeds_ints = (int(x) for x in seeds_line.split(': ')[1].split(' '))
seeds = list(zip(seeds_ints, seeds_ints)) # start, length

next(f) # blank line
next(f) # first map starts

dest = []
map_re = re.compile('map')
for l in f:
    l = l.strip()
    if map_re.search(l):
        # new map
        seeds = dest+seeds # copy remaining seed ranges to dest
        dest = []
        print("")
        print(f"seeds: {seeds}")
        continue
    
    if l == "":
        continue
    
    print(l)
    (dest_start, source_start, length) = (int(x) for x in l.split(' '))
    
    new_seeds = []
    for seed in seeds:
        # part overlaps beginning
        if seed[0] < source_start and seed[0] + seed[1] > source_start:
            new_seeds.append((seed[0], source_start - seed[0]))
            seed = (source_start, seed[0] + seed[1] - source_start)
        # part overlaps end 
        if seed[0] <= source_start + length and seed[0] + seed[1] > source_start + length:
            new_seeds.append((source_start + length, seed[0] + seed[1] - source_start - length))
            seed = (seed[0], source_start + length - seed[0] + 1)
        # complete overlap
        if seed[0] >= source_start and seed[0] + seed[1] <= source_start + length:
            dest.append((seed[0] + dest_start - source_start, seed[1]))
            seed = None
        # remaining part
        if seed != None:
            new_seeds.append(seed)
            
    
    
    print(f"new seeds: {new_seeds}")
    print(f"dest: {dest}")
    seeds = new_seeds
    
    display.fill(0)
    display.text(f"{dest_start} {source_start} {length}",0,0)
    display.text(f"{seeds}",0,10)
    display.text(f"{dest}",0,20)
    display.show()

seeds = dest + seeds
min = seeds[0][0]
for loc in seeds:
    if loc[0] < min:
        min = loc[0]
display.text(f"Min: {min}",0,50)
display.show()
print(min)


