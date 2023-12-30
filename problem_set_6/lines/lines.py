import sys
import os

def valid_args(): # Check if command line arguments are valid
    if len(sys.argv) == 0:
        print("Too few command line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command line arguments")
        sys.exit(1)
    else:
        file = sys.argv[1]
        if file.find(".py") == -1: # Check if file is a python file
            print("Not a python file")
            sys.exit(1)
        else:
            return True

def file_exists(): # Check if file exists
    try:
        os.path.exists(sys.argv[1])
        return True        
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def count_lines(): # Count lines in file
    file = open(sys.argv[1], "r")
    lines = 0
    for line in file:
        line = line.strip()
        if line != "" and not line.startswith("#"): # Ignore blank lines and comments
            lines += 1
    return lines

def main():
    if valid_args() and file_exists():
        print(count_lines())

if __name__ == "__main__":
    main()