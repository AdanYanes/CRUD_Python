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
    
def menu(car_dictionary_list, add_car):
    while(True):
        option = input("Introduzca la opcion a realizar, siendo estas: ingresar, eliminar, consultar o finalizar\n")
    
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
                    car_brand = input('Ingrese el modelo del coche que desea buscar\n')
                    consult_especific_car(car_dictionary_list, car_brand.capitalize())
                else:
                    print('No ha elegido ninguna de las opciones anteriores')
            case "finalizar":
                write_file(car_dictionary_list)
                exit(0)
            case _:
                write_file(car_dictionary_list)
                exit(0)


car_dictionary_list = read_file()
menu(car_dictionary_list, add_car)