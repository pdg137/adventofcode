from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
import math
import re

display = Display()

f = open('data08.txt', 'r')

instructions = next(f).strip()
next(f) # blank

map = {}
matcher = re.compile("(\S\S\S) = \((\S\S\S), (\S\S\S)\)")
for line in f:
    m = matcher.match(line.strip())
    map[m.group(1)] = (m.group(2), m.group(3))

    # had to comment this out due to memory fragmentation!
    #display.fill(0)
    #display.text(f"{m.group(1)}: {m.group(2)},{m.group(3)}", 0, 0)
    #display.text(f"Length: {len(map)}", 0, 10)
    #display.show()    

steps = 0
pos = "AAA"
while pos != "ZZZ":
    instruction = instructions[steps%len(instructions)]    
    if instruction == "R":
        pos = map[pos][1]
    else:
        pos = map[pos][0]
    
    steps += 1
    
    display.fill(0)
    display.text(f"{pos}", 0, 0)
    print(f"{steps} {instruction}: {pos}")
    
    display.text(f"Steps: {steps}", 0, 40)
    display.show()

