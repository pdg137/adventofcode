from zumo_2040_robot.display import Display
display = Display()

def isdigit(c):
    return ord(c) >= ord("0") and ord(c) <= ord("9")

f = open('data01.txt', 'r')
total = 0
for l in f:
    line = l.strip()
    nums = (c for c in line if isdigit(c))
    first_num = next(nums)
    last_num = first_num
    for last_num in nums:
        pass
    value = int(first_num+last_num)
    total += value
    
    display.fill(0)
    display.text(line, 0, 0)
    display.text("Value: "+str(value), 0, 20)
    display.text("Total: "+str(total), 0, 30)
    display.show()
    print(line)