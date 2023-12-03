from zumo_2040_robot.display import Display
from zumo_2040_robot.buttons import ButtonB
from zumo_2040_robot.extras.run_file import *
from time import ticks_us, sleep_ms, ticks_diff

display = Display()

names = [
    "Trebuchet?!", "Cube Conundrum", "Gear Ratios", "", "",
    "", "", "", "", "",
    "", "", "", "", "",
    "", "", "", "", "",
    "", "", "", "", ""
    ]

class Button():
    def button_is_pressed(self):
        return rp2.bootsel_button()

    def __init__(self):
        self.last_start = 0
        self.pressed = False
        self.long_pressed = False
        
    def get_press(self):
        b = self.button_is_pressed()
        
        # release
        if self.pressed and not b:
            self.pressed = False
            if not self.long_pressed:
                self.long_pressed = False
                return 0
            self.long_pressed = False
            
        # press
        if not self.pressed and b:
            self.pressed = True
            self.last_start = ticks_us()
            
        # long press
        if self.pressed and not self.long_pressed and ticks_diff(ticks_us(), self.last_start) > 500000:
            self.long_pressed = True
            return 1
        
        return None

button = Button()

group_selected = False
group_start = 1
selected_row = 0
day_selected = False
selected_part = 1

def text(s, x, y, selected):
    global display
    if selected:
        display.fill_rect(x, y-1, len(s)*8, 10, 1)
    display.text(s, x, y, not selected)

def run_program(day, part):
    filename = f"prob{day:02d}_{part}.py"
    name = names[day]
    
    display.fill(0)
    text(f"Day {day:02d}", 0, 1, False)
    text(name, 0, 11, False)
    text(f"Running", 0, 21, False)
    text(f"  {filename}...", 0, 31, False)
     
    display.show()
    
    sleep_ms(1000)
    
    run_file(filename)
    while button.get_press() != 0:
        pass

while True:
    press = button.get_press()
    display.fill(0)
    
    if not day_selected and not group_selected:
        if press == 0:
            group_start = (group_start + 5) % 25
        elif press == 1:
            group_selected = True
            selected_row = 0
    elif not day_selected and group_selected:
        if press == 0:
            selected_row = (selected_row + 1) % 6
        elif press == 1 and selected_row == 5:
            group_selected = False
        elif press == 1:
            day_selected = True
            selected_part = 1
    elif day_selected:
        if press == 0:
            selected_part = (selected_part + 1) % 3
        elif press == 1:
            if selected_part == 0:
                day_selected = False
            else:
                day = group_start + selected_row
                run_program(day, selected_part)
    
    if not day_selected:
        text("Days", 0, 1, group_selected and selected_row == 5)
        text(f'{group_start:02d}-{group_start+4:02d}', 8*5, 1, not group_selected)

        for i in range(5):
            file_selected = (group_selected and i == selected_row)
            day = group_start + i 
            name = names[day-1]
            name += " "*(13-len(name)) # pad to 13 chars
            text(f"{day:02d} {name}", 0, 15+10*i, file_selected)
    else:
        day = group_start + selected_row
        text(f"Day {day}", 0, 1, False)
        text(names[day-1], 0, 11, False)
        
        text("Part 1", 8, 31, selected_part == 1)
        text("Part 2", 120-8*6, 31, selected_part == 2)
        text("back", 0, 54, selected_part == 0)

    display.show()
