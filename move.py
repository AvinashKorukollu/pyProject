from .motor import Motor


class Move:
    def __init__(self):
        self.motor1 = Motor(23, 24)
        self.motor2 = Motor(17, 22)
        self.motor3 = Motor(26, 6)
        self.motor4 = Motor(5, 16)

    def move_forward(self):
        self.motor1.forward()
        self.motor2.forward()
        self.motor3.forward()
        self.motor4.forward()

    def move_backward(self):
        self.motor1.reverse()
        self.motor2.reverse()
        self.motor3.reverse()
        self.motor4.reverse()

    def move_right(self):
        self.motor1.reverse()
        self.motor2.reverse()
        self.motor3.stop()
        self.motor4.stop()

    def move_left(self):
        self.motor3.reverse()
        self.motor4.reverse()
        self.motor1.stop()
        self.motor2.stop()
