from machine import UART
import time

uart1 = UART(1, tx=17, rx=18)
#Choose UART port, direct to TX/RX pins

uart1.init(115200, bits=8, parity=None, stop=1)
#Initialize, set baud rate, bits, parity, and stop 初始化，设置波特率，设置字符位数，设置奇偶校验，设置停止位

def test():
    for i in range(50):
        uart1.write('Hello World!') # Write data
        time.sleep(0.5)
        print(uart1.read()) # Read data
        time.sleep(0.5)

test()
