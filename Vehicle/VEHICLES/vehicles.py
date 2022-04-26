class Vehicle:
    def __init__(self, colour, speed, wheel_count):
        self.colour = colour
        self.speed = speed
        self.wheel_count = wheel_count
        
    def __str__(self):
        return 'colour: {self.colour}\nmax_speed: {self.speed}\namount_of_wheels: {self.wheel_count}\n\n'.format(self=self)
    
    def __travel_time__(self, distance, unit):
        if unit == "km":
            return distance / self.speed
        elif unit == "m":
            return (distance/1000) / self.speed
        else:
            print("Not valid unit, this function is only limited to kilometers and meters")
            
class Car(Vehicle):
    def __init__(self, colour, speed, wheel_count, amount_of_seats):
        self.amount_of_seats = amount_of_seats
        super().__init__(colour, speed, wheel_count)
        
        
class Motorbike(Vehicle):
    def __init__(self, colour, speed, wheel_count, producer):
        self.producer = producer
        super().__init__(colour, speed, wheel_count)
        
class Truck(Vehicle):
    def __init__(self, colour, speed, wheel_count, price):
        self.price = price
        super().__init__(colour, speed, wheel_count)