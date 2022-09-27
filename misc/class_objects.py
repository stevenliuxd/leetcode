class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name + " and my color is " + self.color)

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sitDown(self):
        self.isSitting = True
    
    def standUp(self):
        self.isSitting = False

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

p1 = Person("Alice", "aggresive", False)
p2 = Person("Becky", "talkative", True)
p1.robot_owned = r2
p2.robot_owned = r1
r1.talkingto = r2

p1.robot_owned.introduce_self()
r1.talkingto.introduce_self()
