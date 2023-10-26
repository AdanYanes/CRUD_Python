def remove_car(carList, carBrand):
    for x in carList:
        if(carBrand in x.values()):
            carList.remove(x)
    return carList