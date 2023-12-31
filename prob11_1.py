from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
from array import array

display = Display()

f = open('data11.txt', 'r')

col_empty = array('B', [True]*140)
row_empty = array('B', [True]*140)

display.fill(0)
display.text(f"Expanding...", 0,10)
display.show()

for y, line in enumerate(f):
    line = line.strip()
    for x,c in enumerate(line):
        if c == '#':
            col_empty[x] = False
            row_empty[y] = False
            
# now get all the galaxies' coordinates, expanding
sleep_ms(100)
display.fill(0)
display.text(f"Expanding...", 0,10)
display.text(f"Locating...", 0,20)
display.show()
f = open('data11.txt', 'r')
galaxies = []
yadj = 0
for y, line in enumerate(f):
    line = line.strip()
    xadj = 0
    for x, c in enumerate(line):
        if c == '#':
            galaxies.append([x+xadj,y+yadj])
        if col_empty[x]:
            xadj += 1
    if row_empty[y]:
        yadj += 1
        
sleep_ms(100)
display.fill(0)
display.text(f"Expanding...", 0,10)
display.text(f"Locating...", 0,20)
display.text(f"Galaxies: {len(galaxies)}",0, 30)
display.show()
sleep_ms(500)

# dumb way
total = 0
for g1 in galaxies:
    for g2 in galaxies:
        if g1 == g2:
            continue
        total += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])

    display.fill(0)
    display.text(f"Expanding...", 0,10)
    display.text(f"Locating...", 0,20)
    display.text(f"Galaxies: {len(galaxies)}",0, 30)
    display.text(f"Check: {g1}",0, 40)
    display.text(f"Total: {total//2}",0, 50)
    display.show()
