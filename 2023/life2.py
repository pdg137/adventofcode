from zumo_2040_robot.display import Display
import time
import framebuf
from array import array
import random

display = Display()
b = display.renderbuf

b2 = bytearray(1024)
newframe = framebuf.FrameBuffer(b2, 128, 64, framebuf.MONO_VLSB)

f = open('p41.txt')
for y, line in enumerate(f):
    for x, c in enumerate(line.strip()):
        if c != '.':
            newframe.pixel(x + 64 - 36, y+1, 1)

#for i in range(1024):
#   b2[i] = random.getrandbits(8)

@micropython.viper
def get(buf: ptr8, x: int, y: int) -> bool:
    x = x % 128
    y = y % 64
    p = y // 8
    return buf[p*128 + x] & (1 << y % 8) != 0

@micropython.viper
def set(buf: ptr8, x: int, y: int):
    p = y // 8
    buf[p*128 + x] |= 1 << y % 8

@micropython.viper
def clear(buf: ptr8, x: int, y: int): 
    p = y // 8
    buf[p*128 + x] &= 0xff - (1 << y % 8)

@micropython.viper
def iterate():
    start = time.ticks_ms()
    for x in range(128):
        for p in range(8):
            bp = ptr8(b)
            cur = bp[p*128 + x]
            r = bp[p*128 + (x + 1)%128]
            l = bp[p*128 + (x - 1)%128]
            u = bp[((p-1)%8)*128 + x]
            d = bp[((p+1)%8)*128 + x]
            if cur + r + l + u + d == 0:
                continue
            
            for dy in range(8):
                y = int(p*8 + dy)
                count = int(get(b, x - 1, y - 1) + get(b, x, y - 1) + get(b, x + 1, y - 1) + \
                   get(b, x - 1, y) + get(b, x + 1, y) + \
                   get(b, x - 1, y + 1) + get(b, x, y + 1) + get(b, x + 1, y + 1))
                if count == 2:
                    pass
                elif count == 3:
                    set(b2, x, y)
                else:
                    clear(b2, x, y)
    end = time.ticks_ms()
    print(f"{time.ticks_diff(end, start)} ms")

while True:
    display.blit(newframe, 0, 0)
    display.show()
    
    iterate()

