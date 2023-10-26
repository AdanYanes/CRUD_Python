def write_file(list):
    write_save_file = open('src/db/car_list.txt', 'w')
    for value in list:
        write_save_file.write('%s \n' % str(value))
    write_save_file.close()