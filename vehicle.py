class Vehicle:
    def __init__(self, fuel, drive_train, color, name):
        self.fuel = fuel
        self.drive_train = drive_train
        self.color = color
        self.name = name

    def Drive(self):
        print(f"The {self.color} {self.name} drove past. Vrooom!")

    def Turn(self, direction):
        print(f"The {self.name} turned {direction}.")

    def Stop(self):
        print(f"The {self.name} came to a stop.")