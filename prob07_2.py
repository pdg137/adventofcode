from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
import math

display = Display()

f = open('data07.txt', 'r')

hands = list(tuple(l.strip().split()) for l in f)

def to_num(char):
    if char == 'T': return 10
    if char == 'J': return 1
    if char == 'Q': return 12
    if char == 'K': return 13
    if char == 'A': return 14
    return int(char)

def ranker(hand):
    nums = tuple(to_num(c) for c in hand[0])
    no_js = hand[0].replace('J','')
    no_js_count = [ (no_js.count(i),i) for i in set(no_js) ] # tuples of count and letter
    no_js_count.sort(reverse = True)
    j_replacement = (no_js_count + [(0, 'J')])[0][1]
    replaced = hand[0].replace('J',j_replacement)
    
    type = [ replaced.count(i) for i in set(replaced) ]
    type.sort(reverse = True)
    return (type, nums)

display.fill(0)
display.text(f"{len(hands)} hands", 0, 0)
display.text(f"Sorting...", 0, 10)
display.show()

hands.sort(key=ranker)
print(hands)

total = 0
for i, hand in enumerate(hands):
    value = (i+1) * int(hand[1])
    print(f"{i+1}: {hand} - {value}")
    total += value
    
    display.fill(0)
    display.text(f"{hand[0]}", 0, 0)
    display.text(f"{i+1}*{hand[1]} = {value}", 0, 20)
    
    display.text(f"Total: {total}", 0, 40)
    display.show()
