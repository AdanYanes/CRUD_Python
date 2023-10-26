def consult(car_list):
    if(len(car_list) < 1):
        print("La lista esta vacia")
        
    else:
        counter = 1
        for x in range(len(car_list)):
            print((x+1), 'marca:',car_list[x]['brand'], 'modelo:', car_list[x]['model'])
