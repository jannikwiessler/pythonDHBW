from basic_functions import average_value_of_list


def average_mileage(data: list, vehicle_type: str = "") -> float:
    mileage_list = []
    if not vehicle_type:
        mileage_list = [el["mileage"] for el in data]
    else:
        for el in data:
            if el["vehicle_type"] == vehicle_type:
                mileage_list.append(el["mileage"])
    return average_value_of_list(mileage_list)


def average_costs(data: list) -> float:
    return average_value_of_list([el["damage"]["cost"] for el in data])
