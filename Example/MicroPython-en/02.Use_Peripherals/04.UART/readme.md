# Read/Write Data from UART Serial Port

## Peripherals Required

USB to UART module（CH340，CP2102 and more）。

## Software Required

A serial port configuration software and drivers for USB to UART module.

## Connection Method

Connect BPI-Leaf-S3 development board to PC, USB to UART module's RX pin to GPIO17(Leaf-S3's TX pin), TX to GPIO18(Leaf-S3's RX pin), GND to GND, USB to UART module to PC via USB port, this can be with the same PC as the Leaf-S3 or different PCs. 

## Results 

There will be a 1 second interval on BPI-Leaf-S3's PC MicroPython REPL data output from USB to UART moudle.

We can see on USB to UART module's PC serial port configuration software, there will be a string data `Hello World!` outputted by BPI-Leaf-S3.
