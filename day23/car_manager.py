import random
import car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
CAR_SPACE = 3


class CarManager:
    
    
    def __init__(self):
        self.cars = []
        self.level = 0
        self.car_coming = CAR_SPACE


    def create_next_wave(self):
        self.car_coming -= 1
        if self.car_coming > 0:
            return
        
        self.car_coming = CAR_SPACE
        car_amount = random.randint(1, 10)

        if car_amount > 5:
            return
        
        for i in range(car_amount):
            pos_y = random.randint(-280, 270)
            new_car = car.Car(random.choice(COLORS), x=300, y=pos_y)
            self.cars.append(new_car)


    def move_cars(self):

        for da_car in self.cars:
            da_car.forward(STARTING_MOVE_DISTANCE + (self.level * MOVE_INCREMENT))
            if da_car.xcor() < -330:
                self.cars.remove(da_car)
                da_car.clear()

    def collide_player(self, player):
        for da_car in self.cars:
            if player.distance(da_car) < 20:
                return True
        return False
    
    def add_level(self):
        self.level += 1