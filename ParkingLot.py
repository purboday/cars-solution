from threading import Lock
# The parking lot is implemented as a shared buffer.
# Parking a car is like writing to it.
# Removing a car is like removing items from it.
# It is different from a queue or stack because there is no fixed order of adding/removing items.
# Multiple cars can try to park/remove at the same time. So a lock is used.
class ParkingLot():
    # Constructor. A list is used to keep track of available spots. A dictionary is used for te directory.
    def __init__(self,capacity):
        self.capacity = capacity
        self.available = list(range(self.capacity))
        self.directory = {}
        self.lock = Lock()

    def print_directory(self):
        # Print the contents of the directory.
        print("Current directory")
        for car, spot in self.directory.items():
            print("Car: {}, Location: {}".format(car,spot))

    def park_car(self,car):
        # Park a car. The argument is a car object.
        # Acquire lock before modifying internal variables.
        # Returns true if parking is succesfull, otherwise returns false.
        with self.lock:
            if self.available:
                # Items present in available
                self.directory[car.name] = self.available.pop()
                print("{} successfully parked in location {}".format(car.name,self.directory[car.name]))
                return True
            else:
                # availale list is empty
                print("Parking lot full!!")
                return False

    def remove_car(self,car=None):
        # Remove a car. It can work in two ways.
        # If a car object is prided as an argument. It removes the specified car from the spot.
        # If no argument is specified. It removes the car corresponding to the first key of te directory.
        # As per Python documentation, post Pthon 3.7, dict keys are ordered according to their creation.
        # Returns true if car is removed successfully, otherwise returns false.
        # Acquire lock
        with self.lock:
            if not self.directory:
                # directory is empty
                print("Parking lot empty!!")
                return False
            else:
                if car:
                    # Argument given
                    search_for = car.name
                else:
                    # No argument, find the first key from directory
                    search_for = list(self.directory)[0]

                # Check if the key exists in the directory
                spot= self.directory.get(search_for,None)
                if spot:
                    # Key was found
                    self.available.append(self.directory[search_for])
                    del self.directory[search_for]
                    print("{} removed from location {}".format(search_for,spot))
                    return True
                else:
                    # Key was not found
                    print("{} not found!!".format(search_for))
                    return False