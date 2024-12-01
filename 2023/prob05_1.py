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
seeds = [int(x) for x in seeds_line.split(': ')[1].split(' ')]
next(f) # blank line
next(f) # first map starts

dest = list(seeds)
map_re = re.compile('map')
for l in f:
    l = l.strip()
    if map_re.search(l):
        # new map
        seeds = dest
        dest = list(seeds)
        continue
    
    if l == "":
        continue
    
    print(l)
    (dest_start, source_start, length) = (int(x) for x in l.split(' '))
    
    for i, seed in enumerate(seeds):
        if seed >= source_start and seed < source_start + length:
            dest[i] = seed + dest_start - source_start
    
    display.fill(0)
    display.text(f"{dest_start} {source_start} {length}",0,0)
    display.text(f"{seeds}",0,10)
    display.text(f"{dest}",0,20)
    display.show()

min = dest[0]
for loc in dest:
    if loc < min:
        min = loc
display.text(f"Min: {min}",0,50)
display.show()
print(min)

