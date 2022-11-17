class Vehicle:
    def __init__(self,
                 color: str,
                 brand: str,
                 engine: str,
                 max_speed: int,
                 num_of_seats: int,
                 weigth: int):
        self.color = color
        self.brand = brand
        self.engine = engine
        self.max_speed = max_speed
        self.seats = num_of_seats
        self.weight = weigth

    def print_info(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Engine: {self.engine}")
        print(f"Weight: {self.weight}")
        print(f"Speed: {self.max_speed}")
        print(f"Seats: {self.seats}")


