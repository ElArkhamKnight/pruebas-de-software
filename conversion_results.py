"""
Program created to read a file that is assumed to contain only numbers
"""
# filename: print_numbers.py
import sys
import time

class ConversionArray(list):
    """
    Custom class which extends list and does required computation of it's elements
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._binary_numbers = None
        self._hexadecimal_numbers = None

    def _decimal_to_binary(self, number):
        binary_representation = ""

        if number == 0:
            return "0"

        while number > 0:
            remainder = number % 2
            binary_representation = str(remainder) + binary_representation
            number //= 2

        return binary_representation

    def calculate_binary_numbers(self):
        """
        Method used to calculate the binary numbers of the elements that the class contains
        """
        binary_result = {}

        for num in self:
            binary_result[num] = self._decimal_to_binary(num)

        self._binary_numbers = binary_result

    def get_binary_numbers(self):
        """
        Method used to get the binary numbers of the class
        """
        return self._binary_numbers

    def _decimal_to_hexadecimal(self, number):
        hexadecimal_chars = "0123456789ABCDEF"
        hexadecimal_representation = ""

        if number == 0:
            return "0"

        while number > 0:
            remainder = number % 16
            hexadecimal_representation = hexadecimal_chars[remainder] + hexadecimal_representation
            number //= 16

        return hexadecimal_representation

    def calculate_hexadecimal_numbers(self):
        """
        Method used to calculate the hexadecimal numbers of the elements that the class contains
        """
        hexadecimal_result = {}

        for num in self:
            hexadecimal_result[num] = self._decimal_to_hexadecimal(num)

        self._hexadecimal_numbers = hexadecimal_result

    def get_hexadecimal_numbers(self):
        """
        Method used to get the hexadecimal numbers of the class
        """
        return self._hexadecimal_numbers

    def __str__(self):
        result_string = "NUMBER		TC1	BIN	HEX\n"
        hexadecimal_numbers_dict = self.get_hexadecimal_numbers()

        for index, (key, value) in enumerate(self.get_binary_numbers().items()):
            result_string += f"{index+1} {key} {value} {hexadecimal_numbers_dict[key]}\n"

        # Remove the trailing comma and space
        return result_string.rstrip(", ")

def print_numbers(file_path):
    """
    Method to print the numbers that the file contains
    """
    try:
        start_time = time.time()
        with open(file_path, 'r', encoding="utf-8") as file:
            # Read the numbers from the file and convert them to a list
            numbers = []
            for index, line in enumerate(file):
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Error: File contains non-numeric values in line {index+1}")

            custom_array = ConversionArray(numbers)
            custom_array.calculate_binary_numbers()
            custom_array.calculate_hexadecimal_numbers()
            end_time = time.time()
            elapsed_time_ms = (end_time - start_time) * 1000

            print(custom_array)
            print("\n")
            execution_time_result = f"Time of execution: {elapsed_time_ms:.6f} milliseconds"
            print(execution_time_result)
            with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
                # Print the object to the file using the print function
                print(custom_array, file=file)
                print("\n", file=file)
                print(execution_time_result, file=file)


    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    # Check if a file path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py P1/TC2.txt")
        sys.exit(1)

    # Get the file path from the command line argument
    path_to_file = sys.argv[1]

    # Print the numbers from the file
    print_numbers(path_to_file)
