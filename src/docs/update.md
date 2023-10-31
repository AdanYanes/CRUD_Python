# update

The `update` py file represents the funcionality to update cars dictionaries inside the list.

## Description

The file have a function allowing us to use it on the `main` file with the purpose of selecting if the user want to update an specific element or all of them.

## Class Structure

- `update`:
  - Main method: `update_options(car_dictionary_list)`
  - Class variables:
    - `option`: Store the user input for update option
  - Methods:
    - `update_options(car_dictionary_list)`: Method allow the user to select different updating formats.
    - `update_all_elements(car_list, brand, model, new_brand_value, new_model_value)`: Method allow the `update_options` function to update all the elements inside the car dictionary.
    - `update_specific_element(car_list, element, new_element_value)`: Method allow the `update_options` function to update an specific element inside the car dictionary.

## Main Logic

1. option variable:
   - Store the user option on the `update_options` methods and is used to determinate wether to use the `update_all_elements` or the `update_specific_element` method.

2. update_all_elements(car_list, brand, model, new_brand_value, new_model_value):
   - Run through the `car_list` searching for a coincidence with the `brand` and the `model` values. Then print update the dictionary with the `new_brand_value` and `new_model_value`.

3. update_specific_element(car_list, element, new_element_value):
    - Run through the `car_list` and update the coinciding `element` with the `new_element_value`.

## External Dependencies

- *NO EXTERNAL DEPENDENCIES*