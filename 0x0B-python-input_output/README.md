# Python - Input/Output

In this project, I practiced file handling in Python. I used the built-in `with`,
`open`, and `read` functions along with the `json` module to read and write files,
and serialize and deserialize objects with JSON.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files provided by ALX.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                 | Prototype                                       |
| -------------------- | ----------------------------------------------- |
| `0-read_file.py`     | `def read_file(filename=""): -> str`            |
| `1-number_of_lines.py` | `def number_of_lines(filename=""): -> int`    |
| `2-read_lines.py`    | `def read_lines(filename="", nb_lines=0): -> List[str]` |
| `3-write_file.py`    | `def write_file(filename="", text="") -> int`   |
| `4-append_write.py`  | `def append_write(filename="", text="") -> int` |
| `5-to_json_string.py`| `def to_json_string(my_obj) -> str`            |
| `6-from_json_string.py`| `def from_json_string(my_str) -> Any`         |
| `7-save_to_json_file.py`| `def save_to_json_file(my_obj, filename):`   |
| `8-load_from_json_file.py`| `def load_from_json_file(filename): -> Any`  |
| `10-class_to_json.py`| `def class_to_json(obj) -> dict`               |
| `14-pascal_triangle.py`| `def pascal_triangle(n) -> List[List[int]]` |

## Tasks :page_with_curl:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): Python function that reads and prints the contents of a UTF8 text
  file.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): Python function that writes a string to a UTF8 text
  file and returns the number of characters written.

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): Python function that appends a string to the end of a
  UTF8 text file and returns the number of characters appended.

* **3. To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): Python function that returns the JSON string
  representation of an object.

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): Python function that returns the Python object
  represented by a JSON string.

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): Python function that writes an object to a text
  file using JSON representation.

* **6. Create object from a JSON file**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): Python function that creates an object from a
  `.json` file.

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): Python script that stores all command line arguments in a
  Python list and saves it to the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): Python function that returns the dictionary
  description for simple Python data structures (lists, dictionaries, strings,
  integers, and booleans).

* **9. Student to JSON**
  * [9-student.py](./9-student.py): Python class `Student` that defines a student with
    public instance attributes `first_name`, `last_name`, and `age`, and a
    method `to_json()` to return the dictionary representation of a `Student` instance.

* **10. Student to JSON with filter**
  * [10-student.py](./10-student.py): Python class `Student` that defines a student with
    public method `to_json(self, attrs=None)` to return the
    dictionary representation of a `Student` instance. If `attrs` is provided, only
    the specified attributes are represented in the dictionary.

* **11. Student to disk and reload**
  * [11-student.py](./11-student.py): Python class `Student` that defines a student with
    a public method `reload_from_json(self, json)` to replace all
    attributes of the `Student` instance using the key/value pairs provided in `json`.

* **12. Pascal's Triangle**
  * [12-pascal_triangle.py](./12-pascal_triangle.py): Python function that returns a list of lists of
  integers representing Pascal's triangle of size `n`. Returns an empty list if `n <= 0`.

* **13. Search and update**
  * [100-append_after.py](./100-append_after.py): Python function that inserts a line of text into a
  file after each line containing a specified string.

* **14. Log parsing**
  * [101-stats.py](./101-stats.py): Python script that reads lines from standard input and computes
  metrics after every 10 lines or upon receiving a keyboard interruption (`CTRL + C`).
    * Total file size at that point: `File size: <total size>`
    * Status code of each read line, printed in ascending order: `<status code>: <number>`
  * Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
