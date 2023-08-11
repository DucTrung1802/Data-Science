import os
import statistics

FILENAME = "dataset.txt"

def read_numbers_from_file(filename):
    numbers = []
    full_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(full_filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                numbers.append(number)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data in the file. Please ensure the file contains only numbers.")
    
    return numbers


def main():
    number_list = read_numbers_from_file(FILENAME)
    print("List of numbers:", number_list)
    print("Mean: ", statistics.mean(number_list))    
    print("Stddev: ", statistics.stdev(number_list))

if __name__ == "__main__":
    main()


	

