"""
Program created to read a file that is assumed to contain only numbers
"""
# filename: print_numbers.py
import sys
import time

class ConversionObject():
    """
    Class to store number info as well as it's equivalent values in binary and hexadecimal
    """
    def __init__(self):
        self._number = None
        self._bin_number = None
        self._hex_number = None

    def set_number(self, number):
        """
        Method to set the number
        """
        self._number = number

    def get_number(self):
        """
        Method to get the number
        """
        return self._number

    def set_bin_number(self, bin_number):
        """
        Method to set the bin number
        """
        self._bin_number = bin_number

    def get_bin_number(self):
        """
        Method to get the bin number
        """
        return self._bin_number

    def set_hex_number(self, hex_number):
        """
        Method to set the hex number
        """
        self._hex_number = hex_number

    def get_hex_number(self):
        """
        Method to get the hex number
        """
        return self._hex_number

    def __str__(self):
        return f"{self.get_number()} {self.get_bin_number()} {self.get_hex_number()}"
class ConversionArray(list):
    """
    Custom class which extends list and does required computation of it's elements
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._conversion_array = None

    def _decimal_to_binary(self, number):
        """
        Convert one number to binary
        """
        binary_representation = ""
        is_negative = False

        if number < 0:
            is_negative = True
            number = abs(number)

        while number > 0:
            remainder = number % 2
            binary_representation = str(remainder) + binary_representation
            number = number // 2

        if is_negative:
            binary_representation = ''.join(
                ['1' if bit == '0' else '0' for bit in binary_representation]
            )
            binary_representation = '1' + binary_representation

        return binary_representation

    def _decimal_to_hexadecimal(self, decimal_number):
        if decimal_number < 0:
            # Convert negative numbers to 2's complement hexadecimal representation
            hex_digits = "0123456789ABCDEF"
            hex_value = ""
            decimal_number = (1 << 32) + decimal_number  # 2's complement
            while decimal_number > 0:
                remainder = decimal_number % 16
                hex_value = hex_digits[remainder] + hex_value
                decimal_number //= 16
            return hex_value
        else:
            hex_digits = "0123456789ABCDEF"
            hex_value = ""
            while decimal_number > 0:
                remainder = decimal_number % 16
                hex_value = hex_digits[remainder] + hex_value
                decimal_number //= 16
            return hex_value

    def calculate_binary_and_hexadecimal_numbers(self):
        """
        Method used to calculate the hexadecimal numbers of the elements that the class contains
        """
        conversion_array = []

        for num in self:
            conversion_object = ConversionObject()
            try:
                int_num = int(num)
                conversion_object.set_number(int_num)
                binary = self._decimal_to_binary(int_num)
                conversion_object.set_bin_number(binary)
                hexadecimal = self._decimal_to_hexadecimal(int_num)
                conversion_object.set_hex_number(hexadecimal)
                conversion_array.append(conversion_object)
            except ValueError:
                error_value = "#VALUE!"
                conversion_object.set_number(num)
                conversion_object.set_bin_number(error_value)
                conversion_object.set_hex_number(error_value)
                conversion_array.append(conversion_object)

        self._conversion_array = conversion_array

    def get_conversion_array(self):
        """
        Method used to get the hexadecimal numbers of the class
        """
        return self._conversion_array

    def __str__(self):
        result_string = "INDEX		NUMBER	BIN	HEX\n"

        for index, conversion_object in enumerate(self._conversion_array):
            result_string += f"{index+1} {conversion_object}\n"

        # Remove the trailing comma and space
        return result_string

def print_numbers(file_path):
    """
    Method to print the numbers that the file contains
    """
    try:
        start_time = time.time()
        with open(file_path, 'r', encoding="utf-8") as file:
            # Read the numbers from the file and convert them to a list
            numbers = []
            for line in file:
                numbers.append(line.strip())

            custom_array = ConversionArray(numbers)
            custom_array.calculate_binary_and_hexadecimal_numbers()
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
