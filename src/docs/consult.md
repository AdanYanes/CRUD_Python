# consult

The `consult` py file represents the funcionality to consult cars dictionaries inside the list.

## Description

The file have a function allowing us to use it on the `main` file with the purpose of selecting if the user want to consult an specific car or the whole list.

## Class Structure

- `consult`:
  - Main method: `consult_options(car_dictionary_list)`
  - Class variables:
    - `option`: Store the user input for consult option
  - Methods:
    - `consult_options(car_dictionary_list)`: Method allow the user to select different consulting formats.
    - `consult_all_cars(car_list)`: Method allow the `consult_options` function to show all the cars dictionaries inside the car list.
    - `consult_especific_car(car_list, car_brand)`: Method allow the `consult_options` function to show an specific car dictionary inside the car list due to its car brand.

## Main Logic

1. option variable:
   - Store the user option on the `consult_options` methods and is used to determinate wether to use the `consult_all_cars` or the `consult_specific_car` method.

2. consult_especific_car(car_list, car_brand):
   - Run through the `car_list` searching for a coincidence with the `car_brand` value. Then print the dictionary.

3. consult_all_cars(car_list):
    - Run through the `car_list` and print all the dictionaries inside it.

## External Dependencies

- *NO EXTERNAL DEPENDENCIES*