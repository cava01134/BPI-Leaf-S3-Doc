# Hello World

We can start by printing out "Hello World" as the first lesson in learning MicroPython.

> The following examples are operated on Thonny IDE.  You would need to setup Thonny IDE and connect to your development board. Refer to this [guide](https://wiki.banana-pi.org/Micropython_%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA) for more details.

## Using REPL

**REPL** stands for **Read-Eval-Pring-Loop**.

We can fully understand its meaning through practice.

After successfully flashing firmware onto your MicroPython device and connecting it to the computer, make sure Thonny is configured properly, and we can see the shell return the following:

```
MicroPython v1.17 on 2022-01-09; ESP32S3 module with ESP32S3
Type "help()" for more information.
>>> 
```

Notice the `>>>` prompt, we can directly input functions or codes here, pressing 'Enter' key will immediately return with results.

```python
>>> 1+2
3
>>> print("Hello World")
Hello World
>>> 
```

The process is pretty straight forward, it reads our input messages, calculate the values, outputs the results, then awaits for our next input, hence the name REPL.
We can directly communicate with MicroPython devices, unlike the traditional computing languages like C, requiring compiling process in the middle.  Our messages are being directly sent to the chip without compiling, this is a big feature in the Python language, and MicroPython inherited this feature.

MicroPython REPL supports many serial input/output applications, this is another topic to discover, feel free to try other serial communication tools to better understand the meaning of "no compiling required".

>For further applications on REPL, please refer to [MicroPython Official Docs: REPL](https://docs.micropython.org/en/latest/reference/repl.html)

## Interpreter

Thonny IDE not only serves REPL operations, it could also be used as a Python interpreter.

Create a new file then copy the following code:

```python
print(1+2)
print("Hello World")
```

Once finished editing, hit **Save**, you can choose to save it to MicroPython device or locally.  Rename the file to `main.py` makes the MicroPython device execute this file during startup or after reset.  Other `.py` files can be executed when we click `run current script` in Thonny.

![](https://i.imgur.com/tn9Fi3W.png)

Now hit **Run**, this also does not require compiling, the results will be printed in the shell.

```
3
Hello World
```
We could also try the keyboard hotkey **ctrl + D** to reset software, we can see the results being printed again after reset.
