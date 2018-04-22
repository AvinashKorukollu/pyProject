import RPi.GPIO as gpio

class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        gpio.setup(pin1, gpio.OUT)
        gpio.setup(pin2, gpio.OUT)

    def forward(self):
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)

    def reverse(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, True)

    def stop(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, False)
