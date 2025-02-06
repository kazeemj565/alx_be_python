class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)  # Calling the parent class's constructor
        self.year = year
    
    def display_info(self):
        super().display_info()  # Calling the parent class's method
        print(f"Year: {self.year}")

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2022)

# Calling the method
my_car.display_info()
