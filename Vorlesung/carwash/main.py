class Car:
    def __init__(self, color: str = "black", power: int = 169, cylinder: int = 4):
        self.color = color
        self.power = power
        self.cylinder = cylinder
        self.clean_status = {"body": 1,
                             "wheels": 1}

    def run_offroad(self):
        self.clean_status["body"] = 0
        self.clean_status["wheels"] = 0

    def show_clean_status(self):
        print(f"wheels: {self.clean_status['wheels']}")
        print(f"body: {self.clean_status['body']}")


class Ticket:
    def __init__(self, wash_body: bool = True, wash_wheels: bool = True):
        self.wash_body = wash_body
        self.wash_wheels = wash_wheels


class CarWash:
    def __init__(self):
        pass

    @staticmethod
    def wash(car: Car, ticket: Ticket):
        if ticket.wash_body:
            car.clean_status["body"] = 1

        if ticket.wash_wheels:
            car.clean_status["wheels"] = 1


if __name__ == "__main__":
    car = Car(color="black", power=220, cylinder=4)
    car.show_clean_status()
    car.run_offroad()
    car.show_clean_status()
    wash_ticket = Ticket(wash_body=True, wash_wheels=True)
    car_wash_garage = CarWash()
    car_wash_garage.wash(ticket=wash_ticket, car=car)
    car.show_clean_status()
