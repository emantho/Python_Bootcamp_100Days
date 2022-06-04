# Superior class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


# Inferior class which going to inherate
class Fish(Animal):  # 👈 must include superior class name
    def __init__(self):
        super().__init__()  # super class call INPORTANT

    # inside same funct super class must be called
    def breathe(self):
        super().breathe()  # 👈 right after func creation
        print("doing this underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.breathe()
