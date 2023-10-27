def update_specific_element(car_list, element, new_element_value):
    for x in car_list:
        if(element in x['brand']):
            x['brand'] = new_element_value
            return car_list
        elif(element in x['model']):
            x['model'] = new_element_value
            return car_list
        else:
            print('El elemento proporcionado no existe')
            break
        
        
def update_all_elements(car_list, brand, model, new_brand_value, new_model_value):
    for x in car_list:
        if(brand in x['brand'] and model in x['model']):
            x['brand'] = new_brand_value
            x['model'] = new_model_value
            return car_list