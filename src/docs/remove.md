# remove

The `remove` py file represents the funcionality to remove cars dictionaries inside the list.

## Description

The file have a function allowing us to use it on the `main` file with the purpose of selecting if the user want to remove an specific car or clear the list.

## Class Structure

- `remove`:
  - Main method: `remove_options(car_dictionary_list)`
  - Class variables:
    - `option`: Store the user input for remove option
  - Methods:
    - `remove_options(car_dictionary_list)`: Method allow the user to select different removing formats.
    - `remove_especific_car(car_list, car_brand)`: Method allow the `remove_options` function to remove an specific car dictionary inside the car list due to its car brand.

## Main Logic

1. option variable:
   - Store the user option on the `remove_options` methods and is used to determinate wether to use the `car_list.clear()`  or the `remove_specific_car` method.

2. remove_especific_car(car_list, car_brand):
   - Run through the `car_list` searching for a coincidence with the `car_brand` value. Then remove the dictionary.

## External Dependencies

- *NO EXTERNAL DEPENDENCIES*