from VEHICLES.vehicles import Car, Motorbike, Truck, Vehicle

car = Car("red", 50, 4, 4)
motorbike = Motorbike("blue", 70, 2, "Jawa")
truck = Truck("yellow", 40, 10, 4500000)

str1 = Vehicle.__str__(car)
str2 = Vehicle.__str__(motorbike)
str3 = Vehicle.__str__(truck)

print("CAR\n",str1,"MOTORBIKE\n",str2,"TRUCK\n",str3)

time = Vehicle.__travel_time__(car, 100, "km")
print("The travel will take",time, "hours.")