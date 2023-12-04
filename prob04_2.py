from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
import re

display = Display()

f = open('data04.txt', 'r')
total = 0

def print3line(s):
    display.text(s, 0, 0)
    display.text(s[16:], 0, 10)
    display.text(s[32:], 0, 20)

ws = re.compile('\s+')
copies = [1]*198
for l in f:
    line = l.strip()
    
    (game, numbers) = line.split(':')
    (winning, picked) = numbers.split('|')	
    winning_nums = set(int(x) for x in ws.split(winning.strip()))
    picked_nums = set(int(x) for x in ws.split(picked.strip()))
    result = winning_nums & picked_nums
    
    # count this round's copies
    value = copies[0]
    
    # use up this round's copies
    copies = copies[1:]
    
    # prepare copies for next round
    for i in range(len(result)):
        copies[i] += value   
    
    print(line)
    print(result)
    print(value)
    print(copies)
    display.fill(0)
    print3line(line)
    total += value
    display.text(f"Value: {value}",0,40)
    display.text(f"Total: {total}",0,50)
    display.show()

print(total)
