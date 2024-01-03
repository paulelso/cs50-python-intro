import csv
import os
import sys

def valid_args():
    try:
        if len(sys.argv) > 3: # Check for too many arguments
            print("Too many command line arguments")
            return False
            sys.exit(1)
        elif len(sys.argv) < 3: # Check for too few arguments
            print("Too few command line arguments")
            return False
            sys.exit(1)
        elif len(sys.argv) == 3: # Check for correct number of arguments
            if os.path.exists(sys.argv[1]):
                return True
            else:
                print(f"Could not read {sys.argv[1]}")
                sys.exit(1)
    except IndexError: # Check for IndexError
        sys.exit(1)
    
def output_formatted_lines(file):
        students = []
        with open(file, 'r') as input_file:
            reader = csv.reader(input_file)
            headers = next(reader)  # Get the headers
            headers.extend(['first', 'last', 'house']) # Add new headers
            for line in input_file:
                last, first, house = line.strip().replace('"', '').replace(", ", ",").split(',')
                students.append([first, last, house])                
                
        with open(sys.argv[2], 'w') as output_file:
            fieldnames = ['first', 'last', 'house']
            headers.extend(fieldnames) # Add new headers
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:                
                writer.writerow({'first': student[0], 'last': student[1], 'house': student[2]})
            
def main():
    if valid_args():
        output_formatted_lines(sys.argv[1])          
    else:
        print("Arguments are not valid")
        sys.exit(1)

if __name__ == "__main__":
    main()  # call main function