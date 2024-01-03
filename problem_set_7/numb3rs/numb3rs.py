import re

def main():
    print(validate(input("IPv4 address: ")))

def validate(ip):
    # declaring the regex pattern for IP addresses
    pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
    if re.match(pattern, ip) is None:
       return False
    else:
        return True     
 
if __name__ == "__main__":
    main()
