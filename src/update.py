def update_specific_element(car_list, element, new_element_value):
    for x in car_list:
        if (element in x['brand']):
            x['brand'] = new_element_value
            return car_list
        elif (element in x['model']):
            x['model'] = new_element_value
            return car_list
        else:
            print('El elemento proporcionado no existe')
            break


def update_all_elements(car_list, brand, model, new_brand_value, new_model_value):
    for x in car_list:
        if (brand in x['brand'] and model in x['model']):
            x['brand'] = new_brand_value
            x['model'] = new_model_value
            return car_list


def update_options(car_dictionary_list):
    option = input(
        'Desea actualizar un elemento o algun apartado en especifico? Ingrese \"Elemento\" o \"Especifico\"\n')
    if (option.lower() == 'elemento'):
        car_brand = input('Ingrese la marca del coche que desea actualizar\n')
        car_model = input('Ingrese el modelo del coche que desea actualizar\n')
        new_car_brand = input('introduzca la nueva marca del coche\n')
        new_car_model = input('introduzca el nuevo modelo del coche\n')
        update_all_elements(car_dictionary_list, car_brand.capitalize(
        ), car_model.capitalize(), new_car_brand.capitalize(), new_car_model.capitalize())
    elif (option.lower() == 'especifico'):
        element = input("Ingrese el elemento que desea modificar\n")
        new_element_value = input("Ingrese el nuevo valor para el elemento\n")
        car_dictionary_list = update_specific_element(
            car_dictionary_list, element.capitalize(), new_element_value.capitalize())
    else:
        print('No ha elegido ninguna de las opciones anteriores')
    return car_dictionary_list
