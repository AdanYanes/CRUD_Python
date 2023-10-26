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
from src.consult import consultAllCars, consultEspecificCar
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
                car_dictionary_list = removeCar(car_dictionary_list,carBrand.capitalize())
                print(f'El coche {carBrand.capitalize()} ha sido eliminado')
            case "consultar":
                option = input('Desea consultar todos los coches o alguno en especifico? Ingrese \"Todo\" o \"Especifico\"\n')
                if(option.lower() == 'todo'):
                    consultAllCars(car_dictionary_list)
                elif(option.lower() == 'especifico'):
                    car_brand = input('Ingrese el modelo del coche que desea buscar\n')
                    consultEspecificCar(car_dictionary_list, car_brand.capitalize())
                else:
                    print('No ha elegido ninguna de las opciones anteriores')
            case "finalizar":
                write_file(car_dictionary_list)
                exit(0)
            case _:
                write_file(car_dictionary_list)
                exit(0)


car_dictionary_list = read_file()
menu(car_dictionary_list, addCar)