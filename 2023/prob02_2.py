from zumo_2040_robot.display import Display
import re

display = Display()

display.text("Day 2:", 0, 0)
display.text("Cube Conundrum", 0, 10)
display.show()

f = open('data02.txt', 'r')
total = 0
game_matcher = re.compile("^Game (\d+): (.*)$")
splitter = re.compile("[,;]\s+")

def print3line(s):
    display.text(s, 0, 0)
    display.text(s[16:], 0, 10)
    display.text(s[32:], 0, 20)

def get_power(balls):
    pieces = splitter.split(balls)
    red_min = 0
    green_min = 0
    blue_min = 0
    for piece in pieces:
        (num, color) = piece.split(' ')
        num = int(num)
        if color == "red" and num > red_min:
            red_min = num
        if color == "green" and num > green_min:
            green_min = num
        if color == "blue" and num > blue_min:
            blue_min = num
    return red_min*green_min*blue_min  

for l in f:
    line = l.strip()
    result = game_matcher.match(line)
    game = int(result.group(1))
    balls = result.group(2)
    print(balls)
    display.fill(0)
    print3line(balls)
    
    display.text("Game: "+str(game), 0, 34)
    power = get_power(balls)
    print(power)
    display.text("Power: "+str(power), 0, 44)
    total += power
    display.text("Total: "+str(total), 0, 54)
    
    display.show()
print(total)