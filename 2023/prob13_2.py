from zumo_2040_robot.display import Display
import time
from array import array
import re

display = Display()

bits = list(2**i for i in range(20))
def differ_by_smudge(left, right):
    smudges = 0
    for i, l in enumerate(left):
        r = right[i]
        diff = l ^ r
        if diff == 0:
            continue
        elif diff in bits:
            smudges += 1
        else:
            return False
    return smudges == 1

def check_reflection(values):
    print(values)
    for i in range(1, len(values)):
        left = values[max(0, 2*i-len(values)):i]
        right = values[i:2*i]
        print(f"check {i}: {left} {right}")
        right.reverse()
        if differ_by_smudge(left, right):
            print(f"found {i}")
            return i
    print("no reflection")
    return 0

f = open('data13.txt', 'r')
total = 0
y = 0
line_values = []
column_values = None
display.fill(0)
display.show()

def update_total():
    global total
    h = check_reflection(line_values)
    l = check_reflection(column_values)
    add = 100 * h + l
    total += add
    
    if h:
        display.line(54, 4*h+3, 54 + 4*len(column_values)+7, 4*h + 3, 1)
    if l:
        display.line(54 + 4*l+3, 0, 54 + 4*l + 3, 4*len(line_values)+7, 1)
        
    display.text(str(add), 0, 0)
    display.text(str(total), 0, 10)
    display.show()
    if h and l:
        print("ERROR")
        quit()
    #time.sleep_ms(250)

for line in f:
    line = line.strip()

    if line == "":
        update_total()
        y = 0
        line_values = []
        column_values = None
        display.fill(0)
        continue
    
    line_value = 0
    if not column_values:
        column_values = [0]*len(line)
    
    for x, c in enumerate(line):
        if c == '#':
            line_value += 2**x
            column_values[x] += 2**y
            display.fill_rect(54+ 4*x+4, 4*y+4, 3, 3, 1)
    
    line_values.append(line_value)
    y += 1

update_total()

print(total)
