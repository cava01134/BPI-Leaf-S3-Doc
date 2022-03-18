from machine import Pin
from neopixel import NeoPixel
import time

def rainbow(num=1,level=25,delay=100):
    #num:set total looping LED number
    #level: set brighness level, ranging from 0~255
    #delay:set interval between each change
    def write_all(num,delay,red,green,blue):
        for j in range (num):
            np[j] = (red,green,blue)
        np.write()
        time.sleep_ms(delay)
    
    red,green,blue = level,0,0
    
    rainbow_step_list2 = [(0,1,0),(-1,0,0),(0,0,1),(0,-1,0),(1,0,0),(0,0,-1)]
    
    for step in rainbow_step_list2:
        for i in range (level):
            red+=step[0]
            green+=step[1]
            blue+=step[2]
            write_all(num,delay,red,green,blue)
            #print(red,green,blue)

pin_48 = Pin(48, Pin.OUT)#Set GPIO48 as WS2812 output signal pin
np = NeoPixel(pin_48, 1,bpp=3, timing=1)
# Creates an NeoPixel object "np" on GPIO 48, set looping LED number 1, bpp=3, timing=1在GPIO48上创建一个NeoPixel对象，设置数量1，bpp=3为RGB模式，4为RGBW模式，timing=1为800kHz，0为400kHz
# bpp = 3 stands for RGB mode, bpp = 4 stands for RGBW mode
# timing = 1 stands for 800kHz, timing = 0 stands for 400kHz

while True:
    #Rainbow LED loop
    rainbow(num=1,level=25,delay=10)
    #print("RAM used = {RAM_used}KB".format(RAM_used = gc.mem_alloc()/1024))
    #gc.collect()

    © 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
