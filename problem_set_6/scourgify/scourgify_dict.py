import csv
import os
import sys

def valid_args():
    try:
        if len(sys.argv) > 3:
            print("Too many command line arguments")
            return False
            sys.exit(1)
        elif len(sys.argv) < 3:
            print("Too few command line arguments")
            return False
            sys.exit(1)
        elif len(sys.argv) == 3:
            if os.path.exists(sys.argv[1]):
                return True
            else:
                print(f"Could not read {sys.argv[1]}")
                sys.exit(1)
    except IndexError:
        sys.exit(1)
    
def output_formatted_lines(file):
        my_dict = {}
        with open(file, 'r') as input_file:
            reader = csv.reader(input_file)
            headers = next(reader)  # Get the headers
            headers.extend(['first', 'last', 'house']) # Add new headers
            for line in input_file:
                last, first, house = line.strip().replace('"', '').replace(", ", ",").split(',')
                my_dict.update({first: [last, house]})
                sorted_dict = dict(sorted(my_dict.items(), key=lambda x : x[1] )) # Sort dictionary by last name

        with open('after.csv', 'w') as output_file:
            fieldnames = ['first', 'last', 'house']
            headers.extend(fieldnames) # Add new headers
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            for key, value in sorted_dict.items():
                writer.writerow({'first': key, 'last': value[0], 'house': value[1]})
            
def main():
    if valid_args():
        output_formatted_lines(sys.argv[1])          
    else:
        print("Arguments are not valid")
        sys.exit(1)

if __name__ == "__main__":
    main()  # call main function