import sys
import os
import csv

def valid_args():
    try:
        if len(sys.argv) > 3:
            print("Too many command line arguments")
            sys.exit(1)
        else:
             if sys.argv[1] == "before.csv" and os.path.exists(sys.argv[1]):
                return True 
    except IndexError:
        print("Too few command line arguments")
        sys.exit(1)
    
def format_lines(file):
        my_dict = {}
        with open(file, 'r') as input_file:
            reader = csv.reader(input_file)
            headers = next(reader)  # Get the headers
            headers.extend(['first', 'last', 'house']) # Add new headers
            for line in input_file:
                first, last, house = line.strip().replace('"', '').replace(", ", ",").split(',')
                my_dict.update({first: [last, house]})
        return my_dict
        
def main():
    if valid_args():
        before_file = sys.argv[1]
        print(format_lines(before_file))          
    else:
        print("Arguments are not valid")
        sys.exit(1)

if __name__ == "__main__":
    main()  # call main function


"""
before_file = sys.argv[1]
after_file = sys.argv[2]
my_dict = {}
with open(before_file, 'r') as csv_file:
    next(csv_file)  # Skip the first line
    for line in csv_file:
        first, last, house = line.replace('"', '').replace(", ", ",").strip().split(',')
        my_dict.update({first: [last, house]})
        
with open(after_file, 'w', newline='') as csv_file:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in my_dict.items():
        writer.writerow({'first': key, 'last': value[0], 'house': value[1]})

"""