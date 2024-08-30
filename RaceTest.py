from Car import Car, Convertible

def main():
    # Create the objects
    car1 = Car("Prius",5,"ABC1234", 121, 53)
    car2 = Convertible("Porsche Boxster", 2, "DEF4321", 265, 32)
    # Call method with appropriate command for the convertible
    car2.toggle_roof("lower")

    # Start race
    while car1.curr_speed < 200 and car2.curr_speed < 200:
        car1.accelerate_step(0.2)
        print("{}:{}".format(car1.name,car1.curr_speed))
        car2.accelerate_step(0.2)
        print("{}: {}".format(car2.name,car2.curr_speed))

if __name__ == "__main__":
    main()
