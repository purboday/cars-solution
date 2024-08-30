from Car import Car,Convertible
from ParkingLot import ParkingLot
from threading import Thread

# Each car is implemented as a separate thread that tries to call the park method of thhe parking lot.
# Thus mltiple cars can try to access the parking lot methods at the same time/
# The lock allows only one car to park/unpark at any one time

def parking_thread(car,lot):
    # Helper function for each car thread.
    # It tries to park the car.
    # If unsuccesful, it removes another car and tries again.
    parked = lot.park_car(car)
    while not parked:
        lot.remove_car()
        parked = lot.park_car(car)

def main():
    # Create cars and a parking lot
    cars = [Car("Prius",5,"ABC1234", 121, 53)]
    cars.append(Convertible("Porsche Boxster", 2, "DEF4321", 265, 32))
    cars.append(Car("Civic",5,"NXG2345", 181, 42))
    cars.append(Car("Elantra",5,"HYE8965",147,37))
    cars.append(Convertible("Ford Mustang",2,"FRM3231",310,25))

    lot1 = ParkingLot(3)

    # Initialize threads for each car
    threads=[]
    for car in cars:
        threads.append(Thread(target=parking_thread, args=(car,lot1)))

    # Start the thread execution
    for thr in threads:
        thr.start()

    # Wait for threads to terminate
    for thr in threads:
        thr.join()

    # Print the final directory contents
    lot1.print_directory()

if __name__=="__main__":
    main()