from Car import Car,Convertible
from ParkingLot import ParkingLot

def test_parking_full():
    car1 = Car("Prius",5,"ABC1234", 121, 53)
    car2 = Convertible("Porsche Boxster", 2, "DEF4321", 265, 32)
    car3 = Car("Civic",5,"NXG2345", 181, 42)
    car4 = Car("Elantra",5,"HYE8965",147,37)

    lot1 = ParkingLot(3)

    res1 = lot1.park_car(car1)
    res2 = lot1.park_car(car2)
    res3 = lot1.park_car(car3)
    res4 = lot1.park_car(car4)

    assert (res1 and res2 and res3 and not res4)

