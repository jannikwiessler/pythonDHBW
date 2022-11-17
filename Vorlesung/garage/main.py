import json
from vehicle import Vehicle
from garage import Garage


if __name__ == "__main__":
    vehicle_list = json.load(open("vehicle_data.json"))
    fleet = [Vehicle(
        brand=vehicle["vehicle_brand"],
        color=vehicle["color"],
        engine=f"{vehicle['engine']['cylinder']}-Cyl",
        num_of_seats=vehicle["seats"],
        weigth=vehicle["weight"],
        max_speed=vehicle['engine']["max_speed"]
    ) for vehicle in vehicle_list]
    garage = Garage(capacity=6, fleet=fleet)
    garage.dashboard.show()