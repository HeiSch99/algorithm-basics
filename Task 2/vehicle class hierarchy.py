# Root class
class Vehicle:
    def __init__(self, make, model, wheels):
        self.make = make
        self.model = model
        self.wheels = wheels

    def __str__(self):
        return f"{self.make} {self.model} with {self.wheels} wheels."


# Intermediate classes
class PassengerVehicle(Vehicle):
    def __init__(self, make, model, wheels = 4, seat_capacity = 4):
        super().__init__(make, model, wheels)
        self.seat_capacity = seat_capacity

class UtilityVehicle(Vehicle):
    def __init__(self, make, model, wheels = 6, cargo_capacity = 1000):
        super().__init__(make, model, wheels)
        self.cargo_capacity = cargo_capacity

class Cars(PassengerVehicle):
    def __init__(self, make, model, wheels = 4, seat_capacity = 5):
        super().__init__(make, model, wheels, seat_capacity)


# Specific classes
class Motorcycle(Vehicle):
    def __init__(self, make, model, wheels = 2):
        super().__init__(make, model, wheels)

class Sedans(Cars):
    def __init__(self, make, model, wheels = 4, seat_capacity = 5):
        super().__init__(make, model, wheels, seat_capacity)
        self.body_type = "sedan"

class Convertibles(Cars):
    def __init__(self, make, model, wheels = 4, seat_capacity = 4):
        super().__init__(make, model, wheels, seat_capacity)
        self.roof_type = "convertible"

class FireEngine(UtilityVehicle):
    def __init__(self, make, model, wheels = 6, water_capacity = 5000):
        super().__init__(make, model, wheels)
        self.water_capacity = water_capacity

class Trucks(UtilityVehicle):
    def __init__(self, make, model, wheels = 6, cargo_capacity = 2000):
        super().__init__(make, model, wheels, cargo_capacity)


# Alternative set of Classes with inheritance hierarchy based on the terrain
class WaterVehicle(Vehicle):
    def __init__(self, make, model, wheels = 0, hull_type = "displacement"):
        super().__init__(make, model, wheels)
        self.hull_type = hull_type

    def __str__(self):
        super().__str__()
        return f"{self.make} {self.model} with {self.hull_type} hull."

class Ship(WaterVehicle):
    pass

class Boat(WaterVehicle):
    def __init__(self, make, model, hull_type):
        super().__init__(make, model, hull_type)

class PowerBoat(Boat):
    def __init__(self, make, model, hull_type):
        super().__init__(make, model, hull_type)
        self.hull_type = "v-shape"

class AirVehicle(Vehicle):
    def __init__(self, make, model, wing_span):
        super().__init__(make, model)
        self.wing_span = wing_span

class Airplane(AirVehicle):
    pass

class Helicopter(AirVehicle):
    pass

# Example
if __name__ == "__main__":
    sedan = Sedans("Toyota", "Camry")
    convertible = Convertibles("Mazda", "MX-5")
    fire_engine = FireEngine("Pierce", "Arrow XT")
    power_boat = PowerBoat("Fountain", "34 SC", hull_type = "v-shape")

    print(sedan)
    print(convertible)
    print(fire_engine)
    print(power_boat)