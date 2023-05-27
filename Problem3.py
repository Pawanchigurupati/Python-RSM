class Vehicle:
    def __init__(self,make,model,year):
        self.make =make
        self.model = model
        self.year=year

    def start(self):
        print("The" , self.make, self.model, "started ")

    def stop(self):
        print("The", self.make, self.model ,"stopped")

    def display(self):
        print(f"Make:",self.make)
        print(f"Model:",self.model)
        print(f"Year:",self.year)


class Car(Vehicle):
    def __init__(self,make,model,year,numofDoors,fuel):
        super().__init__(make, model,year)
        self.numofDoors=numofDoors
        self.fuel=fuel


class Motorcycle(Vehicle):
    def __init__(self,make,model,year,topSpeed):
        super().__init__(make,model,year)
        self.topSpeed =topSpeed


class Truck(Vehicle):
    def __init__(self,make,model,year,cargoCapacity,numofAxles):
        super().__init__(make,model,year)
        self.cargoCapacity =cargoCapacity
        self.numofAxles=numofAxles

myCar =Car("Toyota", "Supra",2004, 2, "Petrol")
myMotorcycle=Motorcycle("RoyalEnfeild","Classic",2018, 280)
myTruck=Truck("Tata","strom",2019,"1000 kg",3)

myCar.start()
myCar.display()
myCar.stop()

print()

myMotorcycle.start()
myMotorcycle.display()
myMotorcycle.stop()

print()

myTruck.start()
myTruck.display()
myTruck.stop()
