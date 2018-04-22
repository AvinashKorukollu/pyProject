import sys, termios, tty, os, time
import RPi.GPIO as gpio
from .move import Move

trigger_pin = 18
echo_pin = 25
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

if __name__ == '__main__':
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
