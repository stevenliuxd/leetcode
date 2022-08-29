class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        print("My color is " + self.color)

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()

