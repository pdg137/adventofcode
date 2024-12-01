#from zumo_2040_robot.display import Display
#from time import ticks_us, sleep_ms
from array import array
import re

class Display:
    def text(self, s, x, y):
        print(s)
    def show(self):
        pass
    def fill(self, i):
        pass

display = Display()

def make_re(groups):
    r = '[\.\?]*'
    r += '[\.\?]+'.join('[\#\?]'*g for g in groups)
    r += '[\.\?]*$'
    return re.compile(r)

def possible(pattern, groups):
    in_group = False
    group_count = 0
    for c in pattern:
        if c == '?':
            return True
        elif c == '.' and in_group:
            if group_size < groups[group_count-1]:
                return False
            in_group = False
        elif c == '#':
            if not in_group:
                in_group = True
                group_size = 0
                group_count += 1
                if group_count > len(groups):
                    return False
            group_size += 1
            if group_size > groups[group_count-1]:
                return False
    # the last one must match
    return group_count == len(groups) and group_size == groups[-1]

def matches(pattern, groups):
    dots = re.compile('\.+')
    patterns = [dots.sub('.',pattern)]
    muls = [1]
    
    m = 0
    while len(patterns) > 0:
        #print(str(m)+" "+str(patterns))
        #print(str(muls))
        p = patterns.pop(0)
        mul = muls.pop(0)
        
        i = p.find('?')
        if i == -1: # no more choices
            if possible(p, groups):
                m += mul
            continue

        s1 = dots.sub('.', p[:i] + '.' + p[i+1:])
        s2 = (p[:i] + '#' + p[i+1:])
        
        if possible(s1, groups):
            if s1 in patterns:
                muls[patterns.index(s1)] += mul
            else:
                patterns.append(s1)
                muls.append(mul)
        if possible(s2, groups):
            if s2 in patterns:
                muls[patterns.index(s2)] += mul
            else:
                patterns.append(s2)
                muls.append(mul)
                
    return m

def matches_line(line):
    (pattern, group_string) = line.split(' ')
    pattern = '?'.join([pattern]*5)
    groups = list(int(s) for s in group_string.split(','))*5
    return matches(pattern, groups)

def print3line(s):
    display.text(s, 0, 0)
    display.text(s[16:], 0, 10)
    display.text(s[32:], 0, 20)

f = open('data12.txt', 'r')

total = 0
for line in f:
    print(line.strip())
    count = matches_line(line)
    print(count)
    total += count
    display.fill(0)
    print3line(line)
    display.text(f"count: {count}", 0, 40)
    display.text(str(total), 0, 50)
    display.show()
    
print(total)
