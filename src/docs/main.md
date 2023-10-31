# main

The `main` py file represents the main entry point of the program.

## Description

The program allow us to store and alter in a .txt file a List of dictionaries representing cars.

## Class Structure

- `main`:
  - Main method: `menu(car_dictionary_list)`
  - Class variables:
    - `car_dictionary_list`: List variable storing all the dictionaries.
  - Methods:
    - `menu(car_dictionary_list)`: Menu containing all the options the users can do.

## Main Logic

1. car_dictionary_list variable:
   - After reading the `car_list.txt` file, store all the dictionaries on it.

2. menu:
   - Main logic of the app. Ask the user for an input based on several options.

## External Dependencies

- `write_file`: Used for saving the `car_dictionary_list` data into `car_list.txt` file.
- `read_file`: Used for saving into `car_dictionary_list` the data from `car_list.txt` file.
- `consult_options`: Used for choosing the consulting options on the menu.
- `consult_options`: Used for choosing the consulting options on the menu.
- `remove_options`: Used for choosing the removing options on the menu.
- `update_options`: Used for choosing the updating options on the menu.
- `add_car`: Used for adding a car dictionary into the `car_dictionary_list` list.
