import ast

def read_file():
    read_save_file = open('src/db/car_list.txt', 'r')
    returnable_list = []
    
    for value in read_save_file:
        returnable_list.append(ast.literal_eval(value))
    
    read_save_file.close()
    return returnable_list