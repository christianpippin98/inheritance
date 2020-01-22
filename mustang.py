from vehicle import Vehicle

class Mustang(Vehicle):
    def __init__(self, fuel, drive_train, color, name):
        super().__init__(fuel, drive_train, color, name)

    def Turn(self, direction):
        print(f"The {self.name} drifts {direction} around the corner at 130mph!")
