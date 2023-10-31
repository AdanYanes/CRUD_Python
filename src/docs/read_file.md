# read_file

The `read_file` py file represents the funcionality to read the a text file and return the dictionaries on it.

## Description

The file have a function allowing us to use it on the `main` file with the purpose of saving the car dictionaries from the `db.txt` file into the `car_dictionary_list`.

## Class Structure

- `read_file`:
  - Main method: `read_file`
  - Class variables:
    - `read_save_file`: Store an instance of the file.
    - `returnable_list`: A list made for storing all the dictionaries and be returned after that.
  - Methods:
    - `read_file()`: Method allow the `main` to read a file and extract the data.

## Main Logic

1. read_save_file variable:
   - Creates an instance of a file and it is being used after in a for loop to extract each of the values from it.

2. for `value` in `read_save_file` loop:
   - Creates a loop allowing us to extract all the values in `read_save_file` and store them on `returnable_list` list.

## External Dependencies

- *NO EXTERNAL DEPENDENCIES*