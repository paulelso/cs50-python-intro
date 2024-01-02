import sys
import os

def valid_args(): # Check if command line arguments are valid
    try:
        file = sys.argv[1]
        if len(sys.argv) > 2: # There should only be one command line argument
            print("Too many command line arguments")
            sys.exit(1)
        elif file.find(".py") == -1: # Check if file is a python file
            print("Not a python file")
            sys.exit(1)
        else: # If file is a python file, return True
            return True
    except IndexError: # If there are no command line arguments, exit
        print("Too few command line arguments")
        sys.exit(1)

def file_exists(): # Check if file exists
    try:
        os.path.exists(sys.argv[1])
        return True        
    except FileNotFoundError:
        print(f"{sys.argv[1]} does not exist")
        sys.exit(1)

def count_lines(): # Count lines in file
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File does not exist")
        exit(1)
    lines = 0
    for line in file:
        line = line.strip()
        if line != "" and not line.startswith("#"): # Ignore blank lines and comments
            lines += 1
    return lines

def main():    
    print(count_lines())

if __name__ == "__main__":
    if valid_args() and file_exists():
        main()