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

def check_balls(balls):
    pieces = splitter.split(balls)
    for piece in pieces:
        (num, color) = piece.split(' ')
        num = int(num)
        if color == "red" and num > 12:
            return False
        if color == "green" and num > 13:
            return False
        if color == "blue" and num > 14:
            return False
    return True  

for l in f:
    line = l.strip()
    result = game_matcher.match(line)
    game = int(result.group(1))
    balls = result.group(2)
    print(balls)
    display.fill(0)
    print3line(balls)
    
    display.text("Game: "+str(game), 0, 34)
    if check_balls(balls):
        print("pass")
        display.text("Result: pass", 0, 44)
        total += game
    else:
        print("fail")
        display.text("Result: fail", 0, 44)
    display.text("Total: "+str(total), 0, 54)
    
    display.show()
print(total)