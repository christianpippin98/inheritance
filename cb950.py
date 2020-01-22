from vehicle import Vehicle

class CB950(Vehicle):
    def __init__(self, fuel, drive_train, color, name):
        super().__init__(fuel, drive_train, color, name)

    def Stop(self):
        print(f"The {self.name} tried to stop too quickly and threw the passenger in the ditch!")