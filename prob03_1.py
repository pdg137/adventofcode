from zumo_2040_robot.display import Display
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
                yield (start, i)
                start = -1
    if start != -1:
        yield (start, i+1)

def get_part_positions(line, symbol_line1, symbol_line2, symbol_line3):
    nums = list(get_num_positions(line))
    for num_pos in nums:
        for i in range(num_pos[0]-1, num_pos[1]+1):
            if i < 0 or i >= len(symbol_line1) or i >= len(symbol_line2) or i >= len(symbol_line3):
                continue
            if is_symbol(symbol_line1[i]) or is_symbol(symbol_line2[i]) or is_symbol(symbol_line3[i]):
                yield num_pos
                break

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
    
    parts = get_part_positions(last_line1, last_line2, last_line1, line)
    for part in parts:
        part_number = int(last_line1[part[0]:part[1]])
        print(part_number)
        total += part_number
    
    print(last_line1)
    display.fill(0)
    print3line(last_line1)
    display.text("Total: "+str(total),0,50)
    display.show()
    
    last_line2 = last_line1
    last_line1 = line

print(total)