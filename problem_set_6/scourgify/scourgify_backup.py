import sys
import os
import csv

def valid_args():
    try:                
        if len(sys.argv) > 3:
            print("Too many command line arguments")
            sys.exit(1)
        else:
            return True        
    except IndexError:
        print("Too few command line arguments")
        sys.exit(1)

def check_file():
    try:
        if os.path.exists(sys.argv[1]) and sys.argv[1] == "before.csv":
            return True
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def format_line(line):
    if isinstance(line, list):
        line = ','.join(line)
    #formatted_line = line.strip().replace('"', '').replace("' ", "'").replace(", ", ",").split(',')
    first, last, house = line.strip().replace('"', '').replace("' ", "'").replace(", ", ",").split(',')
    my_list = [first, last, house]

def read_csv_file(file_path, formatted_lst):
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the headers
        # Add new headers
        headers.extend(['first', 'last', 'house'])
        for row in reader:
            formatted_row = format_line(row)
            formatted_lst.append(formatted_row)
    return formatted_lst

def export_csv_file(after_file, formatted_lst):
    with open(after_file, 'w', newline='') as csvfile:
        #fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in formatted_lst:
            writer.writerow(row)

def main():
    formatted_lst = []
    if valid_args() and check_file():
        before_file = sys.argv[1]
        after_file = sys.argv[2]
        read_csv_file(before_file, formatted_lst)
        #export_csv_file(after_file, formatted_lst)
        print(formatted_lst)

if __name__ == "__main__":
    main()  # call main function
