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


my_car = Car(10, -1, True) # Car() is called a constructor because it constructs the object

print(my_car.speed, my_car.sterring, my_car.throttle)







