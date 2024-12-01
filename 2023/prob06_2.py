from zumo_2040_robot.display import Display
from time import ticks_us, sleep_ms
import math

display = Display()

f = open('data06.txt', 'r')

times = int(''.join(next(f).strip().split()[1:]))
records = int(''.join(next(f).strip().split()[1:]))
games = [(times,records)]

total = 1
delta = 0.0001
for game in games:
    # distance = n * (t-n) = tn - n^2 > record
    # n^2 - tn + r = 0
    # n = (t +- sqrt(t^2 - 4r))/2
    t = game[0]
    r = game[1] + delta # make sure to beat it
    min = (t - math.sqrt(t**2 - 4 * r))/2
    max = (t + math.sqrt(t**2 - 4 * r))/2
    value = math.floor(max) - math.ceil(min) + 1
    total *= value
    
    display.fill(0)
    display.text(str(game), 0, 0)
    display.text(f"{min:.2f} - {max:.2f}", 0, 10)
    display.text(f"{value} ways to win", 0, 20)
    
    display.text(f"Total: {total}", 0, 40)
    display.show()
    
    print(game)
    print([min,max])
    print(value)
    sleep_ms(500)