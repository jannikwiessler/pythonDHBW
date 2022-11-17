from vehicle import Vehicle


class Dashboard:
    def __init__(self):
        self.num_of_vehicles = 0
        self.num_of_vehicles_per_brand = {}
        self.average_weight_of_vehicles = 0

    def calc_num_of_vehicles(self, fleet: list[Vehicle]):
        self.num_of_vehicles = len(fleet)

    def calc_num_of_vehicles_per_brand(self, fleet: list[Vehicle]):
        for vehicle in fleet:
            if vehicle.brand in self.num_of_vehicles_per_brand.keys():
                self.num_of_vehicles_per_brand[vehicle.brand] += 1
            else:
                self.num_of_vehicles_per_brand[vehicle.brand] = 1

    def calc_average_weight_of_vehicles(self, fleet: list[Vehicle]):
        self.average_weight_of_vehicles = sum([vehicle.weight for vehicle in fleet]) / self.num_of_vehicles

    def update(self, fleet: list[Vehicle]):
        self.calc_num_of_vehicles(fleet=fleet)
        self.calc_num_of_vehicles_per_brand(fleet=fleet)
        self.calc_average_weight_of_vehicles(fleet=fleet)

    def show(self):
        print(f"Total number of vehicles in garage: {self.num_of_vehicles}")
        print(f"Number if vehicles per brand: {self.num_of_vehicles_per_brand}")
        print(f"Average weight of vehicle in garage: {self.average_weight_of_vehicles}")

class Garage:
    def __init__(self, capacity: int, fleet: list[Vehicle]):
        self.capacity = capacity
        self.fleet = fleet[0:capacity]
        self.dashboard = Dashboard()
        self.dashboard.update(fleet=self.fleet)

    def print_fleet(self):
        for car in self.fleet:
            print("--------")
            car.print_info()
