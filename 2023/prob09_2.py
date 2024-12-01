from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms

display = Display()

f = open('data09.txt', 'r')

def diff(values):
    for i in range(len(values)-1):
        yield values[i+1] - values[i]

def any(values):
    for v in values:
        if v:
            return True
    return False

total = 0
for line in f:
    values = list(int(s) for s in line.split())
    
    t = values[0]
    s = 1
    while(any(values)):
        values = list(diff(values))
        s *= -1
        t += values[0]*s
    print(t)
    total += t   
    display.fill(0)
    display.text(f"Value: {t}", 0, 30)
    display.text(f"Sum: {total}", 0, 40)
    display.show()

 


