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
starting_positions = []
for line in f:
    map[line[0:3]] = (line[7:10], line[12:15])

for key in list(map.keys()):
    if key[2] == 'A':
        starting_positions.append(key)

print(starting_positions)
steps = 0
positions = list(starting_positions)
finish_positions = list([] for i in range(len(starting_positions)))
while steps < 100000:
    instruction = instructions[steps%len(instructions)]
    steps += 1
    found_smaller_than_two = False
    #print(f"{steps} {instruction} {positions}")
    for i, pos in enumerate(positions):
        if instruction == "R":
            pos = map[pos][1]
        else:
            pos = map[pos][0]
        positions[i] = pos
        if pos[-1] == 'Z':
            print(f"{steps}: {i} finished")
            finish_positions[i].append((steps, pos))
        if len(finish_positions[i]) < 2:
            found_smaller_than_two = True
    if not found_smaller_than_two:
        break

# you need to compute the GCD of the repeats
print(finish_positions)
    
display.fill(0)
display.text("Check terminal", 0, 0)
display.text("output.", 0, 10)

display.text(f"Steps: {steps}", 0, 40)
display.show()


