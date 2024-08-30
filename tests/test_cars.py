import pytest
from Car import Car, Convertible, Roof

def test_car_acc_invalid_input():
    with pytest.raises(AssertionError):
        car1 = Car("Prius",5,"ABC1234", 121, 53)
        car1.accelerate_step(-2)

def test_car_acc_valid_input():
    car1 = Car("Prius",5,"ABC1234", 121, 53)
    car1.accelerate_step(0.5)
    assert car1.curr_speed == 0.5*0.03*121

def test_convertible_toggle_roof_open():
    car2 = Convertible("Porsche Boxster", 2, "DEF4321", 265, 32)
    car2.toggle_roof("lower")
    assert car2.roof_pos == Roof.OPEN

def test_convertible_toggle_roof_invalid_cmd():
    with pytest.raises(AssertionError):
        car2 = Convertible("Porsche Boxster", 2, "DEF4321", 265, 32)
        car2.toggle_roof("release")