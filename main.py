#  Necesitamos una lista
# Lo tocho debe ser una funcion
# Creamos un fichero en e que ingresar datos y guardarlos enuna lista
# Los datos seran una marca de coche y un modelo
# Los datos seran streams
# Los datos se introducen por consola
# Cada objeto del coche sera un diccionario
# Eliminar por marca

from src.helpers.write_file import write_file
from src.helpers.read_file import read_file
from src.consult import consult_all_cars, consult_especific_car
from src.create import add_car
from src.remove import remove_especific_car
from src.update import update_all_elements, update_specific_element
    
def menu(car_dictionary_list):
    while(True):
        option = input("Introduzca la opcion a realizar, siendo estas: ingresar, eliminar, consultar, actualizar o finalizar\n")
    
        match option:
            case "ingresar":
                add_car(car_dictionary_list)
            case "eliminar":
                option = input('Desea eliminar todos los coches o alguno en especifico? Ingrese \"Todo\" o \"Especifico\"\n')
                if(option.lower() == 'todo'):
                    car_dictionary_list.clear()
                elif(option.lower() == 'especifico'):
                    car_brand = input('Ingrese el modelo del coche que desea eliminar\n')
                    car_dictionary_list = remove_especific_car(car_dictionary_list, car_brand.capitalize())
                else:
                    print('No ha elegido ninguna de las opciones anteriores')
            case "consultar":
                option = input('Desea consultar todos los coches o alguno en especifico? Ingrese \"Todo\" o \"Especifico\"\n')
                if(option.lower() == 'todo'):
                    consult_all_cars(car_dictionary_list)
                elif(option.lower() == 'especifico'):
                    car_brand = input('Ingrese la marca del coche que desea buscar\n')
                    consult_especific_car(car_dictionary_list, car_brand.capitalize())
                else:
                    print('No ha elegido ninguna de las opciones anteriores')
            case "actualizar":
                option = input('Desea actualizar un elemento o algun apartado en especifico? Ingrese \"Elemento\" o \"Especifico\"\n')
                if(option.lower() == 'elemento'):
                    car_brand = input('Ingrese la marca del coche que desea actualizar\n')
                    car_model = input('Ingrese el modelo del coche que desea actualizar\n')
                    new_car_brand = input('introduzca la nueva marca del coche\n')
                    new_car_model = input('introduzca el nuevo modelo del coche\n')
                    update_all_elements(car_dictionary_list, car_brand.capitalize(), car_model.capitalize(), new_car_brand.capitalize(), new_car_model.capitalize())
                elif(option.lower() == 'especifico'):
                    element = input("Ingrese el elemento que desea modificar\n")
                    new_element_value = input("Ingrese el nuevo valor para el elemento\n")
                    car_dictionary_list = update_specific_element(car_dictionary_list, element.capitalize(), new_element_value.capitalize())
                else:
                    print('No ha elegido ninguna de las opciones anteriores')
            case "finalizar":
                write_file(car_dictionary_list)
                exit(0)
            case _:
                write_file(car_dictionary_list)
                exit(0)


car_dictionary_list = read_file()
menu(car_dictionary_list)