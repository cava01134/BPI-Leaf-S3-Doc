from machine import Pin
from neopixel import NeoPixel
import time 
pin_48 = Pin(48) #BPI-Leaf-S3  #NeoPixel LED onboard GPIO 48
np = NeoPixel(pin_48, 1,bpp=3, timing=1)  # Initialize NeoPixel
while True:
    np[0] = (25,25,25)   #3 same values indicates white light
    np.write()  #LED on
    time.sleep_ms(250) #250ms interval
    np[0] = (0,0,0) #LED off
    np.write()
    time.sleep_ms(250)
