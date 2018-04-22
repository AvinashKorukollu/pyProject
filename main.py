import sys, termios, tty, os, time
import RPi.GPIO as gpio
from .move import Move

gpio.setmode(gpio.BCM)

class Move:
    def __init__(self):
    	gpio.setup(23, gpio.OUT)
        gpio.setup(24, gpio.OUT)
        gpio.setup(17, gpio.OUT)
        gpio.setup(22, gpio.OUT)
        gpio.setup(26, gpio.OUT)
        gpio.setup(6, gpio.OUT)
        gpio.setup(5, gpio.OUT)
        gpio.setup(16, gpio.OUT)

    def move_forward(self):
        gpio.output(23, True)
        gpio.output(24, False)
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(26, True)
        gpio.output(6, False)
        gpio.output(5, True)
        gpio.output(16, False)

    def move_backward(self):
        gpio.output(23, False)
        gpio.output(24, True)
        gpio.output(17, False)
        gpio.output(22, True)
        gpio.output(26, False)
        gpio.output(6, True)
        gpio.output(5, False)
        gpio.output(16, True)

    def move_right(self):
        gpio.output(23, True)
        gpio.output(24, False)
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(26, False)
        gpio.output(6, False)
        gpio.output(5, False)
        gpio.output(16, False)

    def move_left(self):
        gpio.output(23, False)
        gpio.output(24, False)
        gpio.output(17, False)
        gpio.output(22, False)
        gpio.output(26, False)
        gpio.output(6, True)
        gpio.output(5, False)
        gpio.output(16, True)


move = Move()


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


button_delay = 0.2

try:
    char = getch()
    if char == "p":
        exit(0)
    elif char == "a":
        move.move_left()
    elif char == "d":
        move.move_right()
    elif char == "w":
        move.move_forward()
    elif char == "s":
        move.move_backward()
    else:
        time.sleep(button_delay)

except KeyboardInterrupt:
	print('KeyboardInterrupt')

finally:
	print('gpio cleanup')
	gpio.cleanup()