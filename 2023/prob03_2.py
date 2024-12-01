from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
import re

display = Display()
display.text("Day 3:", 0, 0)
display.text("Gear Ratios", 0, 10)
display.show()

f = open('data03.txt', 'r')
total = 0

def print3line(s):
    display.text(s, 0, 0)
    display.text(s[16:], 0, 10)
    display.text(s[32:], 0, 20)

def isdigit(c):
    return ord(c) >= ord("0") and ord(c) <= ord("9")

def is_symbol(c):
    return not isdigit(c) and c != '.'
            
def get_num_positions(s):
    start = -1
    for i, c in enumerate(s):
        if start == -1:
            if isdigit(c):
                start = i
        else:
            if not isdigit(c):
                yield (start, i, int(s[start:i]))
                start = -1
    if start != -1:
        yield (start, i+1, int(s[start:i+1]))

def get_gear_ratios(line, line1, line2, line3):
    
    nums = list(get_num_positions(line1)) +\
        list(get_num_positions(line2)) +\
        list(get_num_positions(line3))
    
    for i, c in enumerate(line):
        if c != '*': continue
        connected_numbers = []
        for num in nums:
            if num[0]-1 <= i and i < num[1]+1:
                connected_numbers.append(num[2])
        print(connected_numbers)
        if len(connected_numbers) == 2:
            yield connected_numbers[0]*connected_numbers[1]

last_line2 = '.'*140 # no symbols
last_line1 = '.'*140 # no symbols
def f_plus_1():
    for l in f:
        yield l
    yield '.'*140

for l in f_plus_1():
    line = l.strip()
    if(len(line) > 140):
        raise Exception("line length: "+str(len(line)))
    
    gear_ratios = get_gear_ratios(last_line1, last_line2, last_line1, line)
    for gear_ratio in gear_ratios:
        print(gear_ratio)
        total += gear_ratio
    
    print(last_line1)
    display.fill(0)
    print3line(last_line1)
    display.text("Total: "+str(total),0,50)
    display.show()
    
    last_line2 = last_line1
    last_line1 = line

print(total)