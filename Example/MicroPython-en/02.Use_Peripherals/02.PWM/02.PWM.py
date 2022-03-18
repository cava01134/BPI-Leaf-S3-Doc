from machine import Pin, PWM
import time

PWM_LED = PWM(Pin(13)) #Create PWM object "PWM_LED" on GPIO13
PWM_LED.freq(1000) #Set frequency
PWM_LED.duty(0) #Set duty cycle, 0≤duty≤1023, 10bit precision

while True:
    for i in range(0,1024,1):
       PWM_LED.duty(i)
       time.sleep_ms(2)
    for i in range(1022,0,-1):
       PWM_LED.duty(i)
       time.sleep_ms(1)
    #adjust sleep_ms 修改sleep_ms parameters can change "LED breathing" frequency
