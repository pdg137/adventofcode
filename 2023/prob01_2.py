from zumo_2040_robot.display import Display
display = Display()

def isdigit(c):
    return ord(c) >= ord("0") and ord(c) <= ord("9")

num_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def getnums(line):
    global num_names
    for i in range(len(line)):
        substring = line[i:]
        if isdigit(substring[0]):
            yield int(substring[0])
            continue
        for i, name in enumerate(num_names):
            if substring.startswith(name):
                yield i

f = open('data01.txt', 'r')
total = 0
for l in f:
    line = l.strip()
    print(line)
    nums = getnums(line)
    
    first_num = next(nums)
    last_num = first_num
    for last_num in nums:
        pass
    value = first_num*10+last_num
    total += value
    
    display.fill(0)
    display.text(line, 0, 0)
    display.text(line[16:], 0, 10)
    display.text(line[32:], 0, 20)
    display.text("Value: "+str(value), 0, 40)
    display.text("Total: "+str(total), 0, 50)
    display.show()
    #sleep_ms(1)