#  Necesitamos una lista
# Lo tocho debe ser una funcion
# Creamos un fichero en e que ingresar datos y guardarlos enuna lista
# Los datos seran una marca de coche y un modelo
# Los datos seran streams
# Los datos se introducen por consola
# Cada objeto del coche sera un diccionario
# Eliminar por marca

from src.helpers.writeFile import write_file
from src.helpers.readFile import read_file
from src.consult import consult
from src.create import addCar
from src.remove import removeCar
    
def menu(car_dictionary_list, addCar):
    while(True):
        option = input("Introduzca la opcion a realizar, siendo estas: ingresar, eliminar, consultar o finalizar\n")
    
        match option:
            case "ingresar":
                addCar(car_dictionary_list)
            case "eliminar":
                carBrand = input('Introduzca la marca del coche a eliminar')
                car_dictionary_list = removeCar(car_dictionary_list,carBrand)
                print(f'El coche {carBrand} ha sido eliminado')
            case "consultar":
                consult(car_dictionary_list)
            case "finalizar":
                write_file(car_dictionary_list)
                exit(0)
            case _:
                write_file(car_dictionary_list)
                exit(0)


car_dictionary_list = read_file()
menu(car_dictionary_list, addCar)