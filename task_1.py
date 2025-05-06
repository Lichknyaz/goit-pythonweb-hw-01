from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory, ABC):
    def create_car(self, make, model):
        return Car(make, model, "US spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US spec")


class EUVehicleFactory(VehicleFactory, ABC):
    def create_car(self, make, model):
        return Car(make, model, "EU spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU spec")


# Використання

# США
us_vehicle = USVehicleFactory()
us_car1 = us_vehicle.create_car("Ford", "Mustang")
us_car1.start_engine()

# ЄС
eu_vehicle = EUVehicleFactory()
eu_moto = eu_vehicle.create_motorcycle("BMW", "R1250")
eu_moto.start_engine()
