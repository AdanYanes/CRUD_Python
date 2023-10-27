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
from src.consult import consult_options
from src.create import add_car
from src.remove import remove_options
from src.update import update_options
    
def menu(car_dictionary_list):
    while(True):
        option = input("Introduzca la opcion a realizar, siendo estas: ingresar, eliminar, consultar, actualizar o finalizar\n")
    
        match option:
            case "ingresar":
                add_car(car_dictionary_list)
            case "eliminar":
                car_dictionary_list = remove_options(car_dictionary_list)
            case "consultar":
                consult_options(car_dictionary_list)
            case "actualizar":
                car_dictionary_list = update_options(car_dictionary_list)
            case "finalizar":
                write_file(car_dictionary_list)
                exit(0)
            case _:
                write_file(car_dictionary_list)
                exit(0)


car_dictionary_list = read_file()
menu(car_dictionary_list)