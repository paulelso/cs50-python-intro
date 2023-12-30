from tabulate import tabulate
import csv
import os
import sys

def valid_args(): # Check if command line arguments are valid
    try:
        file = sys.argv[1]
        if len(sys.argv) > 2: # There should only be one command line argument
            print("Too many command line arguments")
            sys.exit(1)
        elif not file.endswith(".csv"): # Check if file is a CSV file
            print("Not a CSV file")
            sys.exit(1)
        else: # If file is a python file, return True
            return True
    except IndexError: # If there are no command line arguments, exit
        print("Too few command line arguments")
        sys.exit(1)

def get_file(): # Check if file exists
    try:        
        if os.path.exists(sys.argv[1]):
            file = sys.argv[1]
            return file
    except FileNotFoundError:
        print(f"{sys.argv[1]} does not exist")
        sys.exit(1)

def print_prices(file): # Print prices of pizza
    with open(file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        my_list = [row for row in csvreader]
        print(tabulate(my_list, headers="firstrow", tablefmt="grid"))
    
def get_sicilian_price(): # Get regular price of pizza
    my_list = []
    with open('sicilian.csv', newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            my_list.append(row)
        print(tabulate(my_list, headers="firstrow", tablefmt="grid"))
        
def main():
    if valid_args():
        print_prices(get_file())   
        
if __name__ == "__main__":
    main()