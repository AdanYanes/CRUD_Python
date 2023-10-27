def remove_especific_car(car_list, car_brand):
    for x in car_list:
        if(car_brand in x.values()):
            car_list.remove(x)
    return car_list