from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
from array import array

display = Display()

def possibilities(length, groups):
    total_broken = sum(groups)
    if len(groups) == 1:
        for i in range(length-groups[0]+1):
            yield [0]*i+[1]*groups[0]+[0]*(length - i - groups[0])
    else:
        for i in range(length - sum(groups) + 1):
            for l in possibilities(length - i - groups[0] - 1, groups[1:]):
                yield [0]*i + [1]*groups[0] + [0] + l

def matches(pattern, groups):
    count = 0
    for p in possibilities(len(pattern), groups):
        matches = True
        for i, c in enumerate(pattern):
            if c == '?':
                continue # always matches
            elif c == '#' and p[i] == 1:
                continue # both broken
            elif c == '.' and p[i] == 0:
                continue # both working
            matches = False
            break
        if matches:
            count += 1
    return count

def matches_line(line):
    (pattern, group_string) = line.split(' ')
    groups = list(int(s) for s in group_string.split(','))
    return matches(pattern, groups)

def print3line(s):
    display.text(s, 0, 0)
    display.text(s[16:], 0, 10)
    display.text(s[32:], 0, 20)

f = open('data12.txt', 'r')

total = 0
for line in f:
    count = matches_line(line)
    total += count
    display.fill(0)
    print3line(line)
    display.text(f"count: {count}", 0, 40)
    display.text(f"total: {total}", 0, 50)
    display.show()
    
print(total)