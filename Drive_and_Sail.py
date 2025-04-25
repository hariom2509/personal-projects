class Car:
    def __init__(self,max_speed,unit):
        self.max_speed = max_speed
        self.unit =unit

    def __str__(self):
        return f"Car with the maximum speed of {self.max_speed}{self.unit}"

class Boat:
    def __init__(self,max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return f"Boat with the maximum speed of {self.max_speed}"

q = int(input())

for _ in range(q):
    parts = input().split()
    vehicle_type = parts[0]

    if vehicle_type == "car":
        max_speed = int(parts[1])
        unit = parts[2]
        vehicle = Car(max_speed,unit)
        print(vehicle)

    elif vehicle_type =="boat":
        max_speed = int(parts[1])
        vehicle = Boat(max_speed)
        print (vehicle)
    else:
        continue


