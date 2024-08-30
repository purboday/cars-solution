from enum import Enum
# Roof can have two states OPEN or CLOSED.
class Roof(Enum):
    OPEN=1
    CLOSED=2


class Car():
    def __init__(self,name,seats,prod_num,hp,mpg):
        # Constuctor
        self.name = name
        self.seats = seats
        self.prod_num = prod_num
        self.engine = Engine(hp,mpg)
        self.curr_speed = 0
        
    def accelerate_step(self,scale):
        # horse power (hp) = energy/time, energy = force * distance, force = mass * acceleration (acc)
        # Therefore, hp is linearly proportional to acc
        # Standard car with 180 hp has 0-60 time of 10 s
        # (60*5280/10*3600) = k * 180
        # k can be approximated to 0.05 ft s^-2 or 0.03 m h^-1 s^-1
        assert (scale >= -1 and scale <= 1), "Value must be between -1 and 1"
        acc = 0.03 * scale * self.engine.hp
        # current speed can not be negative
        self.curr_speed=max(0,self.curr_speed + acc)

    def print_car_info(self):
        # Prints car information
        print("Name: {}, Type: {}, Production Number: {}, Horse Power: {}".format(self.name,self.__class__.__name__,self.prod_num,self.engine.hp))


class Convertible(Car):
    # Inherits from Car
    def __init__(self, name, seats, prod_num, hp, mpg, convertible=False):
        # Constructor
        super().__init__(name, seats, prod_num, hp, mpg)
        self.roof_pos = Roof.CLOSED
        self.valid_commands = {"lift","lower"}  # set of valid commands for roof

    def toggle_roof(self, command):
        command = command.lower()
        assert command in self.valid_commands, "invalid command {}".format(command)
        if command == "lift" and self.roof_pos == Roof.OPEN:
                self.roof_pos = Roof.CLOSED
                print("{} roof lifted".format(self.name))
        if command == "lower" and self.roof_pos == Roof.CLOSED:
                self.roof_pos = Roof.OPEN
                print("{} roof lowered".format(self.name))

        

class Engine():
    # Engine class.
    def __init__(self,hp,mpg):
        #Constructor. Argument values must be numbers
        self.hp = float(hp)
        self.mpg = float(mpg)