def add_car(list):
    brand = input('Introduce la marca \n')
    model = input('Introduce el modelo\n')
    
    vehicle = {
        'brand': brand,
        'model': model
    } 
    list.append(vehicle)
    return list

