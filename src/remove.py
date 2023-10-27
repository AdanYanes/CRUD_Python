def remove_especific_car(car_list, car_brand):
    for x in car_list:
        if(car_brand in x.values()):
            car_list.remove(x)
    return car_list

def remove_options(car_dictionary_list):
    option = input('Desea eliminar todos los coches o alguno en especifico? Ingrese \"Todo\" o \"Especifico\"\n')
    if(option.lower() == 'todo'):
        car_dictionary_list.clear()
    elif(option.lower() == 'especifico'):
        car_brand = input('Ingrese el modelo del coche que desea eliminar\n')
        car_dictionary_list = remove_especific_car(car_dictionary_list, car_brand.capitalize())
    else:
        print('No ha elegido ninguna de las opciones anteriores')
    return car_dictionary_list