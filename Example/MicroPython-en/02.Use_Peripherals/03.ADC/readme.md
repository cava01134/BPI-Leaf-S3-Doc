# PWM Single Color Breathing LED

## Peripherals Required

One rotation sensor(potentiometer).

![](https://i.imgur.com/mnuHlMR.jpg)

## ADC on ESP32-S3

ESP32-S3 has two **ADC analog to digital converter** integrated inside the chip, measuring from 0mV~3100mV, 12bit resolution, dividing 0mV~3100mV/2^12=4096 levels, each level as one number.

Two ADC modules each have 10 measuring channels, ADC1 measuring GPIO1 ~ 10, ADC2 measuring GPIO11 ~ 20.

## Connecting Method

GND to GND, VCC to 3V3, S output to GPIO11 pin, using ADC2 channel 1 to measure.

GPIO1~20 pins can be used as ADC input pins.

## Code

| Attenuation Values | Measurable Voltage Input Range|
| -------- | -------- |
| ADC.ATTN_0DB     | 0 mV ~ 950 mV     |
| ADC.ATTN_2_5DB   | 0 mV ~ 1250 mV     |
| ADC.ATTN_6DB     | 0 mV ~ 1750 mV     |
| ADC.ATTN_11DB     | 0 mV ~ 3100 mV     |

 1. `ADC(*，atten)`Initializes GPIO1's ADC channel, adjust `atten` to set attenuation values, this controls the chip's measurable voltage input range, if not set, it is set `atten=ADC.ATTN_0DB` by default or previously set values.
 2. Use `ADC.atten()` function to adjust attenuation values after initializing a ADC channel.
 3. `ADC.read()` function reads ADC and returns its values, ESP32-S3's ADC returns 12bit precision data.
 4. `ADC.read_u16()`function reads ADC then returns 16bit data.
 5. `ADC.read_uv()`function takes an analog reading and return an integer value with units of microvolts `uV`. The return value only has'mV' resolution(meaning it will always be the multiplier of 1000 microvolts.

Wi-Fi feature also uses ADC2, that said, trying to measure ADC2 channel GPIO11 ~ 20 while Wi-Fi is active will cause abnormal analog readings.

It is recommended to use `ADC.read_uv()` to read voltage values, it is based on ADC analog to digital converter's characteristics to return a value in decimal constant, making it more reliable than other reading methods, also divide the value by 1000 `ADC.read_uv()//1000` to get `mV` resolution value. 

Print out `ADC.read()` or `ADC.read_u16()` directly will return decimal numerical value, use `hex()` function to convert data type into hexadecimals, for example, use `hex(ADC.read())` or `bin()` functions to convert data type into binary.
