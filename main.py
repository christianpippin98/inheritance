from mustang import Mustang
from cybertruck import Cybertruck
from cb950 import CB950
from four_runner import Four_Runner
from urus import Urus
from vehicle import Vehicle

tri_motor = Cybertruck("electric", "all-wheel", "silver", "Cybertruck")
nineteen_sixty_nine = Mustang("diesel", "front wheel", "red", "Mustang")
cafe_racer = CB950("gasoline", "two-wheel", "brown", "CB950")
lamborghini = Urus("gasoline", "all-wheel", "yellow", "Urus")
mudder = Four_Runner("gasoline", "4x4", "burnt-orange", "4Runner")

lamborghini.Drive()
tri_motor.Drive()
cafe_racer.Drive()
mudder.Drive()
nineteen_sixty_nine.Drive()

lamborghini.Turn("left")
tri_motor.Turn("left")
cafe_racer.Turn("left")
mudder.Turn("left")
nineteen_sixty_nine.Turn("left")

lamborghini.Turn("right")
tri_motor.Turn("right")
cafe_racer.Turn("right")
mudder.Turn("right")
nineteen_sixty_nine.Turn("right")

lamborghini.Stop()
tri_motor.Stop()
cafe_racer.Stop()
mudder.Stop()
nineteen_sixty_nine.Stop()