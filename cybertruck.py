from vehicle import Vehicle

class Cybertruck(Vehicle):
    def __init__(self, fuel, drive_train, color, name):
        super().__init__(fuel, drive_train, color, name)

    def Drive(self):
        print(f"The {self.color} {self.name} drove by. Did you hear it? Nah, me neither.")