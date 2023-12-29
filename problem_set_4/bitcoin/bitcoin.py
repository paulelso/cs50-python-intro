import requests
import sys

def main():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r.raise_for_status()  # Raise an exception if the request fails
        data = r.json()
        price = data["bpi"]["USD"]["rate"]
        price = round(float(price.replace(",", "")), 4)  # Set price to four decimal places
        qty = get_input()
        result = round((qty * price), 4)  # Set result to four decimal places
        print(f"${result:,.4f}")  # Adds thousands comma separator to the result
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making the API request: {e}")
        exit(1)

def get_input():
    try:
        user_input = float(sys.argv[1])
        return user_input
    except ValueError:
        print("Command-line argument is not a number")
        exit(1)
    except IndexError:
        print("Missing command-line argument")
        exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
        exit(1)