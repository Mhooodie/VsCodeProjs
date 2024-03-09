print('running script')

# car_speed = 10
# car_steering = -1
# car_throttle = True

#Object
class Car: # Object is an instance of a class
    #Function
    def __init__(self, speed, steering, throttle):
        self.speed = speed
        self.sterring = steering
        self.throttle = throttle

    def adjust_speed(self, adjustment): # Making function on class which gives function to every car(object) we create
        self.speed = self.speed + adjustment


my_car = Car(10, -1, True) # Car() is called a constructor because it constructs the object
your_car = Car(50, 0, False)


print(my_car.speed, my_car.sterring, my_car.throttle)
print(your_car.speed, your_car.sterring, your_car.throttle)

print("----------------------------------------------------------")

my_car.adjust_speed(60)
your_car.adjust_speed(-20)

print(my_car.speed, my_car.sterring, my_car.throttle)
print(your_car.speed, your_car.sterring, your_car.throttle)





