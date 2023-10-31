# write_file

The `write_file` py file represents the funcionality to storage the `car_dictionary_list` list content inside a text file.

## Description

The file have a function allowing us to use it on the `main` file with the purpose of saving the car dictionaries from the `car_dictionary_list` variable into the `db.txt` file.

## Class Structure

- `write_file`:
  - Main method: `write_file`
  - Class variables:
    - `write_save_file`: Store an instance of the file.
  - Methods:
    - `write_file()`: Method allow the `main` to save into a text file.

## Main Logic

1. write_save_file variable:
   - Creates an instance of a file and it is being used after in a for loop to extract each of the values from it.

2. for `value` in `read_save_file` loop:
   - Creates a loop allowing us to extract all the values from `car_dictionary_list` and write them on `db.txt` file.

## External Dependencies

- *NO EXTERNAL DEPENDENCIES*